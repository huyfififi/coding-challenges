# Step 2

## 勉強会参加者の方々のPR

- [ryosuketcさんのPR](https://github.com/ryosuketc/leetcode_arai60/pull/26)
    - 確かに、level-order traversal -> BFSの先入観が強く、`queue`を使用したが、(Pythonだったら) 普通に`for`ループでいいのか。ハッとさせられた。
    - Step 1の発想自体はほぼ同じ。ネストを下げてでもlevelごとに処理する方法の方がわかりやすいのではという指摘がなされている。
- [tokuhiratさんのPR](https://github.com/tokuhirat/LeetCode/pull/26)
    - `current`という語を使うことを意図的に避けられていて、関連リンクも貼られている。
        - 私は`current_level` vs `next_level`という対応関係がある変数の置き方をStep 1でしたが、確かに`nodes`, `next_nodes`の方が、一般的な使われ方ではない"current"を避けつつ、意図が明確に伝わる。真似しよう。
    - ryosuketcさんと同じく、queueを用いずにforループでBFSを処理されている。みなさんこのパターンがすんなり書けるようなので、私も選択肢として持っておいた方がいいな。
    - `level_ordered_values`、多少長いが何が入っているのかわかりやすい。
        - 私はStep 1では、良い名前が思いつかなかったので、短い関数であることもあって、返す値に`answer`と命名してしまっていた。

## その他考えたこと

### `while (true)`について

自分自身ではうまく説明できなかったが、何となく Step 1 で用いた`while (true)`という形が嫌だな、と感じたのでDiscordで検索をかけてみた。

- [while Trueは、あまり好みでないです。終わるのがどこなのか、目の縦の移動が必要になるからです。](https://github.com/fuga-98/arai60/pull/26#discussion_r2004906584)
- [Step2では修正されていますが、`while True`を使うときは「内部で確実にreturnかbreakが起こり無限ループが発生しないか」というようにかなり身構えますね。個人的にはstep2のような脱出条件とエラーを作っておくほうが心理的に安心します。](https://github.com/tokuhirat/LeetCode/pull/11#discussion_r2080943934)
- [`while True:` と書くと無限ループになっていないか不安になります。...](https://github.com/fuga-98/arai60/pull/23#discussion_r2161159864)

ざっとGoogleした結果も似たような感じか。できるだけ避けていこう。
