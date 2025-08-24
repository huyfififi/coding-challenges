# Step 1

再帰的に新しいNodeを作って繋げる方法が思いついたが、終了条件を設定しないと無限に再帰関数を呼んでしまう。
これは`node_to_close`というmapを持てば、既にあるNodeのクローンを作成したかどうかをチェックできるし、edgeを作る時も使用できる。
(こう書くと何も問題なくすぐに解法が思いついたように聞こえてしまうが、例を追ってみるのと無限ループをどう防ぐか考えることに少し時間がかかった。)

C++におけるnested functionsの書き方がわからなかったのでとりあえずChatGPTが提示した方法の中からテキトーに選んで先に進んだ。

# Step 2

Discord内にこの問題をレビューに回された方はいなさそう (Step 2時点)。

## Nested Functions in C++

[StackOverflow - Can we have functions inside functions in C++?](https://stackoverflow.com/questions/4324763/can-we-have-functions-inside-functions-in-c)

少し古い質問・回答だが、lambdaを使用するか、local classを介する方法が一般的だろうか。私がStep 1で使用した方法もlambdaで、[この回答のコードに](https://stackoverflow.com/a/46566416/16193058)

私の回答の場合

- `[&]` -> 外側のスコープにあるlambdaで使用された変数を参照キャプチャする。`[=]` とすれば値キャプチャ（コピー）になる。変数を指定することもでき、`[&node_to_clone]` のように明示できるが、CloneGraphHelper 自身を再帰呼び出しするためには、ややコードを煩雑にして明示しなければいけなくなる。
- `(Node* node)` -> 引数
- `-> Node*` -> 戻り値の型を明示 (ラムダでは型推論できる場合は省略可能)
- `{ ... }` -> 関数の中身

そもそもテストnested functionを使用するかどうかだが、私はスコープが減らせることの方がテストのしやすさ (後で調べる) よりも今回の場合嬉しく感じるが、まだ強く意見を持つほどの知識と経験がない。
