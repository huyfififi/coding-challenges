# Step 1

Level order traversalといえばBFSというのはすぐに思いついた。C++を書くのが初めてだったので、vectorとqueueのドキュメントを確認しながら書いたが、大きな引っ掛かりは覚えなかった。

Outer loopを `while (true)` とした理由は、例えばPythonで書くと

```python
queue = deque([root])
while queue:  # Outer loop to check queue is not empty
    next_queue = deque()
    while queue:  # Inner loop to pop all nodes in each level
        node = queue.popleft()
        if node is None:
            continue
        # append node.left and node.right to next_queue
```

のような形になり、outer loopとinner loopが同じ条件なのに違う目的で使われることが、やや奇妙で混乱の元になるかなと考えたからだ。が、杞憂かもしれない。
また、今回の場合問題にはならないだろうが、inner loopでouter loopの条件に用いられている変数を変更してしまっていることも、バグの元になりそうで怖かった。

Step 2で他の方々のPRを見てわかったのだが、for loopを使用するかnull pointersをqueueに入れない形なら、うまくまとまりそうだ。

# Step 2

## 勉強会参加者の方々のPRを5つ眺めてみる

- [ryosuketcさんのPR](https://github.com/ryosuketc/leetcode_arai60/pull/26)
    - 確かに、level-order traversal -> BFSの先入観が強く、`queue`を使用したが、普通に`for`ループでいいのか。ハッとさせられた。
    - Step 1の発想自体はほぼ同じ。ネストを下げてでもlevelごとに処理する方法の方がわかりやすいのではという指摘がなされている。
- [tokuhiratさんのPR](https://github.com/tokuhirat/LeetCode/pull/26)
    - `current`という語を使うことを意図的に避けられていて、関連リンクも貼られている。
        - 私は`current_level` vs `next_level`という対応関係がある変数の置き方を、許容範囲かなと思いStep 1で使用したが、確かに`nodes`, `next_nodes`の方が、一般的な使われ方ではない"current"を避けつつ、意図が明確に伝わる。真似しよう。
    - ryosuketcさんと同じく、queueを用いずにforループでBFSを処理されている。みなさんこのパターンがすんなり書けるようなので、私も選択肢として持っておいた方がいいな。
    - `level_ordered_values`、多少長いが何が入っているのかわかりやすい。
        - 私はStep 1では、良い名前が思いつかなかったので、短い関数であることもあって、返す値に`answer`と命名してしまっていた。
- [irohafternoonさんのPR](https://github.com/irohafternoon/LeetCode/pull/29)
    - なるほど、[`std::vector<T,Allocator>::emplace_back`](https://en.cppreference.com/w/cpp/container/vector/emplace_back)という関数を用いて各階層でのvectorを作成しているのか。
        - vectorを別で作成してそのまま[`push_back()`](https://en.cppreference.com/w/cpp/container/vector/push_back)するとコピーが発生するので、この方法の方が処理が減らせそう。
- [colorboxさんのPR](https://github.com/colorbox/leetcode/pull/40)
    - [Range-based for loop](https://en.cppreference.com/w/cpp/language/range-for.html)というものがあるよう。
- [Ryotaro25さんのPR](https://github.com/Ryotaro25/leetcode_first60/pull/28)
    - [C++では参照を受け取ってそこへ直接書き込むことも出来ますね。ご参考までに。`vector<int>& values = level_to_values.emplace_back();`](https://github.com/Ryotaro25/leetcode_first60/pull/28/files#r1729662913)
        - なるほど、こういうことができるのか。
    - レビュワーの方々から、queueにnull pointersを入れない方がわかりやすく収まるとのフィードバックをいただいている。
    - `level_to_values`という命名がわかりやすい。

みなさんのPRを眺めていて、私の「ファーストチョイスとしてqueueやstackにnullやinvalidな値を積んでしまう」クセに気がついた。あまり詳細な記憶がないが、多少余分な処理を行なってしまうにせよ、条件分岐が少なめに抑えられる、という経験則からだろうか。

## その他、回答を作成する間に調べたこと

### `while (true)`について

自分自身ではうまく説明できなかったが、何となく Step 1 で用いた`while (true)`という形が嫌だな、と感じたのでDiscordで検索をかけてみた。

- [while Trueは、あまり好みでないです。終わるのがどこなのか、目の縦の移動が必要になるからです。](https://github.com/fuga-98/arai60/pull/26#discussion_r2004906584)
- [Step2では修正されていますが、`while True`を使うときは「内部で確実にreturnかbreakが起こり無限ループが発生しないか」というようにかなり身構えますね。個人的にはstep2のような脱出条件とエラーを作っておくほうが心理的に安心します。](https://github.com/tokuhirat/LeetCode/pull/11#discussion_r2080943934)
- [`while True:` と書くと無限ループになっていないか不安になります。...](https://github.com/fuga-98/arai60/pull/23#discussion_r2161159864)

ざっとGoogleした結果も似たような感じか。できるだけ避けていこう。
