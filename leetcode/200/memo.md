# Step 1

ダブってもいいからqueueにpushする形で書いたが、queueにpushする前にチェックをする方が余分な処理が省ける、というDiscussionを見かけた記憶がある。
上下左右が同じ座標をpushする可能性があるので、queueにpushする前にチェックしないと、直感的には大体4倍の要素を処理する必要が出てくる。
制約によるが、結構効いてきそうなので、先にチェックした方がいいか...。

# Step 2

## Discord内のPRを10つくらい眺めた

- 結構細かく処理を切り出す方を多く見かけるな (`is_land()`, `traverse()` in BFS など) 。
	- 個人的には切り出すかどうかちょうど迷うくらいの長さだなと感じる。結局処理をちゃんと読んでいくなら、まとまっていた方が、いろんな関数にとんで目が動かされるよりも楽かな...。
	- 複雑な処理を覆って、メインのループを読む時に覚えていなければいけないことを減らすことも理解できる。
- そういえば、今は4方向を予め定義してループを回しているが、ベタ書きした方が読みやすいと幾人かに言われたような記憶が蘇ってきた。
- [`std::vector<bool>`](https://en.cppreference.com/w/cpp/container/vector_bool.html) は 特殊な最適化がなされているよう (?)
	- boolはintegral typeで、`std::vector<bool> v(10);`などで各要素がvalue-initializationされるとzero-initialized -> falseになりそうだが、もう少し後で調べたい。
- `std::pair`の`.first`, `.second`が書いててなんとなく冗長で面倒な気がするのと、Pythonのtupleに慣れているのもあり、 私は`std::pair`よりも`std::tuple`を使用しがちなのだが、要素が二つだとわかっている座標などのデータを扱うとき、`std::pair`を使用される方が多い (というか見かける限り皆さん) 印象。
- Disjoint Set Unionを使用されてる方結構いるな。復習が追いついていないのだが、できるに越したことはないのだろうな。

## constantの変数名

constantをkConstantName のような変数名で定義するのは知っていたのだが、`num_rows`/`num_cols`がconstantにあたるのかどうか自信がなかった。関数というスコープで見ると、不変の値のように感じたので。

[*Variables declared constexpr or const, and whose value is fixed for the duration of the program, are named with a leading "k" followed by mixed case.*][https://google.github.io/styleguide/cppguide.html#Constant_Names]

ということは、関数の中では一定だが呼び出しに応じて変化しうるものにはこのルール (ガイド) は当てはまらさなそうに聞こえる。
Chromium Code Searchで`const\ int\ k[A-Z]`を検索して見ると、全て固定の数字を持つもので、実行中に変わらないものだけだな。だから、`kNumRows`ではなく`num_rows`という名付けで良さそうだ。(自信はないけれど。)

## push-after-checking vs push-before-checking

300x300、要素の全てが1のmatrixに対して queue から取り出した時に範囲・water・visited チェックをする方法と、入れる前にチェックする方法の実行時間を比較するプログラムをLLMに書いてもらって `-O3` でコンパイルして走らせたら以下のようになった。

```
Benchmark: 300x300 matrix (all 1s), 10000 iterations
===========================================

Solution1 (push before check):
  Total time: 13501 ms
  Average time per iteration: 1.3501 ms
  Average time per iteration: 1350.1 microseconds

Solution2 (prune before push):
  Total time: 5501 ms
  Average time per iteration: 0.5501 ms
  Average time per iteration: 550.1 microseconds

Comparison:
  Solution1 (push before check): 13946 ms
  Solution2 (prune before push): 5531 ms
  Solution2 is 2.52142x faster
```

overheadがあるので、queueに同じ座標を入れる回数を 4 -> 1 回に減らした (角・端は元々4回もないが、デカいmatrixだとならして4回だと置ける) から 4x faster とはいかないが、これくらいの数字で2倍以上差が出るのか。

少し悩んだが、今回の場合先にチェックしても後にチェックしても code complexity がそこまで変わらないような気がするので、先にチェックする方法でstep2, 3に進もうとおもう。
