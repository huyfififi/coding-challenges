# Step 1

Level order traversalといえばBFSというのはすぐに思いついた。C++を書くのが初めてだったので、vectorとqueueのドキュメントを確認しながら書いたが、大きな引っ掛かりは覚えなかった。

Outer loopを `while (true)` とした理由は、例えば外側を`while (!queue.empty())`とすると

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

のような形になり、outer loopとinner loopが同じ条件なのに違う目的で使われることが、やや奇妙で混乱の元になるかなと考えたからだ。
また、今回の場合問題にはならないだろうが、inner loopでouter loopの条件に用いられている変数を変更してしまっていることも、バグの元になりそうで怖かった。
が、他の方々をPRを見てみると、杞憂かもしれないな。

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
    - `vector`と`queue`どちらを使うか、私も迷いどころだった :eyes:
- [Ryotaro25さんのPR](https://github.com/Ryotaro25/leetcode_first60/pull/28)
    - [C++では参照を受け取ってそこへ直接書き込むことも出来ますね。ご参考までに。`vector<int>& values = level_to_values.emplace_back();`](https://github.com/Ryotaro25/leetcode_first60/pull/28/files#r1729662913)
        - なるほど、こういうことができるのか。
        - [Return value: (none) (until c++17), A reference to the inserted element. (since C++17)](https://en.cppreference.com/w/cpp/container/vector/emplace_back)とあるので、これをする時はバージョンに気をつけた方がいいな。
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

### null pointer との比較

[Google C++ Style Guide - 0 and nullptr/NULL](https://google.github.io/styleguide/cppguide.html#0_and_nullptr/NULL)

> For pointers (address values), use nullptr, as this provides type-safety.

[C++ Core Guidelines - ES.87: Don’t add redundant == or != to conditions](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines#es87-dont-add-redundant--or--to-conditions)

> `if (p != nullptr) { ... } // redundant !=nullptr, not recommended`
> Often, if (p) is read as “if p is valid” which is a direct expression of the programmers intent, whereas if (p != nullptr) would be a long-winded workaround.

[Odaさんのコメント](https://github.com/nktr-cp/leetcode/pull/3#issuecomment-2840973072)
[Nodaさんのコメント1](https://github.com/ntanaka1984/leetcode/pull/1#discussion_r2179905618)
[Nodaさんのコメント2](https://github.com/konnysh/arai60/pull/7#discussion_r1845470928)

`if (p)`か`if (p != nullptr)`どちらでもいいらしい。私は明示するのが好きなので`nullptr`を使用する方がしっくりくる (が、今のところ好みを強く論じるほどの知識・経験がない)。

### Avoid reallocation with `reserve()`

[cppreference.com - `std::vector`](https://en.cppreference.com/w/cpp/container/vector.html)

> Reallocations are usually costly operations in terms of performance. The reserve() function can be used to eliminate reallocations if the number of elements is known beforehand.

[cppreference.com - `std::vector<T,Allocator>::capacity`](https://en.cppreference.com/w/cpp/container/vector/capacity.html)

> Returns the number of elements that the container has currently allocated space for.

`std::vector` は、保持している要素数が現在の capacity を超えると、より大きな連続メモリ領域を確保し、既存の要素を移動させる（reallocation）。最大要素数が事前にわかっている場合、reserve() であらかじめ必要なメモリ領域を確保しておけば、その範囲内であれば、無駄な reallocation を防ぐことができる。

### TODO: `size_t`
