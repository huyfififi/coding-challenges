# Step 1

## C++を試してみる

今回は試しにC++で書いてみることにする。

ずっとスタートアップ畑のバックエンドエンジニアとしてPythonをメイン扱っていたので、Pythonはある程度不自由なく扱える (根拠のない？) 自信がある。

また、Discordで

> [(サーチにいたので) C++ は5割で Java は4割という感覚です。...](https://discord.com/channels/1084280443945353267/1250696040701497367/1399699477899509893)

という話を見た時、確かに求人を眺めてもかなりC++やJavaのポジションが多い (一方、Pythonの求人はあまり見かけない肌感覚) と感じたことを思い出したので、少し試してみようという気持ちになったからだ。

他にも、[Linusさんのインタビュー動画](https://youtube.com/shorts/ndZW7044PI8?si=g-3NGT8lJ3V4m7Ty)を観て、うまく言語化できないが、Pythonはコンピュータの内部の挙動から距離が遠く、C (今回はC++を使うが) を勉強すればコンピュータへの理解が深まる、ような気がした。

# Step 2

## 勉強会参加者の方々のPR

- [ryosuketcさんのPR](https://github.com/ryosuketc/leetcode_arai60/pull/26)
    - 確かに、level-order traversal -> BFSの先入観が強く、`queue`を使用したが、(Pythonだったら) 普通に`for`ループでいいのか。ハッとさせられた。
    - Step 1の発想自体はほぼ同じ。ネストを下げてでもlevelごとに処理する方法の方がわかりやすいのではという指摘がなされている。
- [tokuhiratさんのPR](https://github.com/tokuhirat/LeetCode/pull/26)
    - `current`という語を使うことを意図的に避けられていて、関連リンクも貼られている。
        - 私は`current_level` vs `next_level`という対応関係がある変数の置き方を、許容範囲かなと思いStep 1で使用したが、確かに`nodes`, `next_nodes`の方が、一般的な使われ方ではない"current"を避けつつ、意図が明確に伝わる。真似しよう。
    - ryosuketcさんと同じく、queueを用いずにforループでBFSを処理されている。みなさんこのパターンがすんなり書けるようなので、私も選択肢として持っておいた方がいいな。
    - `level_ordered_values`、多少長いが何が入っているのかわかりやすい。
        - 私はStep 1では、良い名前が思いつかなかったので、短い関数であることもあって、返す値に`answer`と命名してしまっていた。
- [irohafternoonさんのPR](https://github.com/irohafternoon/LeetCode/pull/29)
    - なるほど、[`std::vector<T,Allocator>::emplace_back`](https://en.cppreference.com/w/cpp/container/vector/emplace_back)という関数を用いて各階層でのvectorを作成しているのか。
    - TODO: 私の方法とどちらが良いのか。
- [colorboxさんのPR](https://github.com/colorbox/leetcode/pull/40)
    - [Range-based for loop](https://en.cppreference.com/w/cpp/language/range-for.html)というものがあるよう。

また、みなさんのPRを眺めていて、私の「ファーストチョイスとしてqueueやstackにnullやinvalidな値を積んでしまう」クセに気がついた。あまり記憶がないが、多少余分な処理を行なってしまうにせよ、条件分岐が少なめに抑えられる、という経験則からだろうか。現時点ではどちらのパターンが明確に優れているのか、判断しかねる。

## その他考えたこと

### `while (true)`について

自分自身ではうまく説明できなかったが、何となく Step 1 で用いた`while (true)`という形が嫌だな、と感じたのでDiscordで検索をかけてみた。

- [while Trueは、あまり好みでないです。終わるのがどこなのか、目の縦の移動が必要になるからです。](https://github.com/fuga-98/arai60/pull/26#discussion_r2004906584)
- [Step2では修正されていますが、`while True`を使うときは「内部で確実にreturnかbreakが起こり無限ループが発生しないか」というようにかなり身構えますね。個人的にはstep2のような脱出条件とエラーを作っておくほうが心理的に安心します。](https://github.com/tokuhirat/LeetCode/pull/11#discussion_r2080943934)
- [`while True:` と書くと無限ループになっていないか不安になります。...](https://github.com/fuga-98/arai60/pull/23#discussion_r2161159864)

ざっとGoogleした結果も似たような感じか。できるだけ避けていこう。
