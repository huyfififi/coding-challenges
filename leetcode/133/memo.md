# Step 1

再帰的に新しいNodeを作って繋げる方法が思いついたが、終了条件を設定しないと無限に再帰関数を呼んでしまう。
これは`node_to_close`というmapを持てば、既にあるNodeのクローンを作成したかどうかをチェックできるし、edgeを作る時も使用できる。
(こう書くと何も問題なくすぐに解法が思いついたように聞こえてしまうが、例を追ってみるのと無限ループをどう防ぐか考えることに少し時間がかかった。)

C++におけるnested functionsの書き方がわからなかったのでとりあえずChatGPTが提示した方法の中からテキトーに選んで先に進んだ。

# Step 2

Discord内にこの問題をレビューに回された方はいなさそう (Step 2時点)。

## Nested Functions in C++

[StackOverflow - Can we have functions inside functions in C++?](https://stackoverflow.com/questions/4324763/can-we-have-functions-inside-functions-in-c)

少し古い質問・回答だが、lambdaを使用するか、local classを介する方法が一般的だろうか。私がStep 1で使用した方法もlambdaで、[この回答](https://stackoverflow.com/a/46566416/16193058)のコードに酷似している。

私の回答の場合

- `[&]` -> 外側のスコープにあるlambdaで使用された変数を参照キャプチャする。`[=]` とすれば値キャプチャ（コピー）になる。変数を指定することもでき、`[&node_to_clone]` のように明示できるが、CloneGraphHelper 自身を再帰呼び出しするためには、ややコードを煩雑にして明示しなければいけなくなる。
- `(Node* node)` -> 引数
- `-> Node*` -> 戻り値の型を明示 (型推論できる場合は省略可能)
- `{ ... }` -> 関数の中身

そもそもlambdaを使用するかどうかだが、私はスコープが減らせることの方がテストのしやすさ (後でまた考える) よりも今回の場合嬉しく感じるが、まだ強く意見を持つほどの知識と経験がない。

## 命名

### lambdaのスタイル

lambdaで作成した関数はlocal variableなので、function nameのではなくvariable nameのスタイルガイドに従うべきなのだろうか。

[Chrome Code Searchを眺めると](https://source.chromium.org/chromium/chromium/src/+/main:ash/wm/desks/desk.cc;l=889?q=%5C%5B%26%5C%5D&ss=chromium%2Fchromium%2Fsrc)

```cpp
auto find_window_to_stack_below = [&](size_t order) -> aura::Window* {
```

という行があったので、variable nameのスタイルガイドのsnake\_caseが適用されているように思う。

### "clone"という名前の使い方

Step 1で使った`clone_neighbor`は関数名のように聞こえるし、英語的に少し変 (？) な感じがするので、step 2では`neighbor_clone`とした。`cloned_neighbor`も良さげだろうか。

### `node` as 引数

step 1で、`cloneGraph()`に与えられている引数の`node`と、lambdaの引数の`node`が同じ名前を使用しているので、混乱の元になると心配になった。`cloning`、`original`、`src`などが思いついたが、自分では判断がつかないので一旦lambdaの引数を`original`と置いて先に進んでみる。

何回かstep 2 \~ step 3を行き来していて思ったのだが、C++にはPythonのようなキーワード引数が存在しないので、呼び出し側からは引数の名前はどうでもいい -> 与えられている`cloneGraph()`の引数の命名を変えても問題がない、と (自信はないが) 考えたので、わかりづらく感じた、最初に与えられているNodeの変数名 `node` を変更してしまうことにした。
`cloneGraph()`の引数としての`node`という変数名は、特定の意味のあるNodeを指しているのに、抽象的過ぎて個人的に嫌だった。

## 実行時間を測ってみる。

Step 1で実行時間をなんとなく推定してみるべきだったがやり忘れたので素直に測ってみる。

試しにBFSの方の実行時間を測ってみる (with -O3 option) と、ノード数100の一本線となるグラフを処理したとき平均で約7000nsくらいかかった。
CPUのクロック周波数が大体数GHzで、一つの命令に対して数クロックかかるので、大雑把に1秒で10^9個くらい (命令の複雑さや他の要素によっては10^8個くらい?) 命令が処理できる -> 1\~10 ns で 1 命令処理できるとおく。
1つのNodeを処理するのにかかった時間は 7000 ns / 100 = 70 ns -> 10\~100 命令くらい?。C++のコードと命令の対応は、今の私には考察しかねるが、大雑把にそれくらいの命令数だと言われると納得してしまうような気がする。

# Step 3

(PR作成後見直していて) そういえば `std::map`は、Red Black TreeなどのBalanced Binary Search Treeで実装されていて、検索や削除は`O(logN)`だったか。今回の場合`N`は最大でも`100`なので、小さい定数に収まるが、`log(2)64 = 6 < log(2)100 < log(2)128 = 7`で、なんとなくこのへんの数倍程度の差も上で測った実行時間に効いてきているのかなと思った。

# Feedback

- C++ではnested functionを頻繁に用いない
- 各instructionが何クロックかかるかは公式のドキュメントにある
	- 例えば [https://www.intel.co.jp/content/www/jp/ja/content-details/679103/instruction-throughput-and-latency.html](https://www.intel.co.jp/content/www/jp/ja/content-details/679103/instruction-throughput-and-latency.html)
	- AMDのRyzenは軽くGoogleしても見つけられなかった。もう少し視野が広がったら見つかるかも。
- [*ただ、命令一つ一つのクロック数は書かれているのですが、実際にはパイプライン、アウトオブオーダー命令実行、複数の計算ユニットによる同時実行等、命令発行ポート、μop等、複雑です。目安程度に考えておくのが良いと思います。*](https://github.com/huyfififi/coding-challenges/pull/32#discussion_r2315641683)
- テストが書きにくくなるのであまり好まれなさそう。
