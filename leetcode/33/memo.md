# Step 1

The Art of Readable Code を読み返していたら

> Prefer first and last for Inclusive Ranges

とあったので、Binary Searchでありがちな`left`, `right`の代わりに使ってみた。

first -> target があるかもしれない範囲の最初 (最小) のインデックス, firstより左にtargetは存在しない
last -> target があるかもしれない範囲の最後 (最大) のインデックス, lastより右にtargetは存在しない

完全初見の時はいくつか場合分けして考えてかなり煩雑なコードになった記憶があるが、Discordでたまたまレビュー依頼が飛んで来て読んだ時に「二つにわったとき左か右 (または両方) がソートされていることを利用する」というのを覚えてしまっていたため、書くのにそこまで時間はかからなかった。

# Step 2

[個人的には、一度最小値を探して、そこを起点として二分探索を行ったほうが、ソースコードをが分かりやすくなると思います。](https://github.com/Ryotaro25/leetcode_first60/pull/47/changes#r1874216886)

なるほど、そういう方法も考えられるか。

[https://github.com/Ryotaro25/leetcode\_first60/pull/47/changes#r1874204977](https://github.com/Ryotaro25/leetcode_first60/pull/47/changes#r1874204977)

> `int middle  = left + (right - left) / 2;`

そういえばオーバーフローを避けるためにこうすべきだった。Pythonだとこういう問題が発生しないので、C++を書く時には気をつけないといけないところだ。

[https://github.com/naoto-iwase/leetcode/pull/26/](https://github.com/naoto-iwase/leetcode/pull/26/)

適切にkeyに渡す関数を設定することで`bisect.bisect_left()`でもいけるのか、凄いな。

if 文 の中に if 文を持ってこないように場合分け・ealry continueする方法も結構取られているな。私は素直に自分の頭の理解をif文にすると `step1.cpp`のようになりそうだが...


なんだか考えれば考えるほどbinary searchの境界条件とかがわからなくなってきた。時間をとってみっちりいろんな形に変形してみて慣れるべきなのだろうが、今は一旦先に進ませてもらおうかな。
