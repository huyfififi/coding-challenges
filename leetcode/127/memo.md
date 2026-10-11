# Step 1

レビュー依頼をされた時に一度解いたことがあったような気がするのだが、内容を忘れていた。いかんせんLeetCode練習会をやり始めてから一年以上経過してしまったので、ある程度仕方がないか。理想を言えば、もっと早足で駆け抜けられたらよかったのだろう。

シンプルな解法が思いつき、他の案が思いつかなかったので、一旦実装した -> `step1_tle_56_out_of_57_passed.py`

文字列の数を N 文字列の長さを L とすると

BFSは、各 word がたかだか 1 回ずつ処理され O(N)、endWord との文字列比較 O(L) とneighbor のループ O(N) で 時間計算量が O(N * (L + N))

`word_to_neighbors` の 構築が時間がかかりそうで、2重ループとハミング距離の計算で O(N^2 * L)。

> 1 <= wordList.length <= 5000

> 1 <= beginWord.length <= 10, endWord.length == beginWord.length, wordList[i].length == beginWord.length

より、ステップ数がだいたい 5000 * 5000 * 10 ~= 3 * 10 ^ 8。Python が大雑把に 10 ^ 6 steps / second の処理が行えるとすると、実行時間は100\~1000秒 だと推測されるが、これは経験的にギリギリ LeetCode で通るのではないかと思った、のだが結果的に TLE になった。

## Hints from ChatGPT

ChatGPT にヒントをもらった。3回くらいヒントを小出しにしてもらってやっと解答に辿り着いた。-> `step1.py`

> Minimal direction: think about whether you really need to compare every pair of words to discover which words are neighbors.

> “What possible neighbor words can I generate from this word?”

> 25 × 10 = 250 — every string exactly one character away from one 10-character word.

チェック・ループするものを工夫して入れ替える問題にこの前も出会ったような気がするが、記憶がない。類題を出されてすぐに解答に辿り着ける自信はまだないが、頭になんとなく入れておこう。

(ただ、この方法だと文字種がごく限られている場合にしかうまくいかないような気がする。)

文字列の数を N 文字列の長さを L とすると

時間計算量: queue に word は高々 1 度しか入らず、各文字列に対して、26 文字 * L positions の候補を検討するが、その時に`list()` と`.join()`を使用している (`O(L)`) ので、総じて `O(NL)`。

空間計算量: 文字列の set、queue、seen に最大で N 個の長さ L の文字列が入るので `O(NL)`

# Step 2

レビュー依頼していただいた時に見た Discord 内の pull requests を見てみる。

[garunitule さんのPR](https://github.com/garunitule/coding_practice/pull/20)

なるほど、`h*t` みたいな形を key として隣接する word を 辞書型で持てば、わざわざ 26 文字種分ループして隣接する文字列の辞書を作らなくても済むな。-> `step2_pattern_matching.py`

空間計算量: O(NL^2), preprocessing で最大 NL 個の pattern key を作成し、それぞれの key が合計 O(L) 文字の substring を保持するため、O(NL^2)。value 側には word への参照が合計 O(NL) 個入るが、pattern key の方が支配的。
時間計算量: O(NL^2), preprocessing が各 word に対して L 個のパターンの substring を作成 (O(L))。また、BFSも最大で N 個の word を処理するが、各文字列に対して L 個のパターンを検討し、substring の作成で O(L)。合計で O(NL^2)。`pattern_to_words[pattern]` は、制約より最大でも 26 個 しか持たないので、O(1) として無視。

[dxxsxsxkx さんのPR](https://github.com/dxxsxsxkx/leetcode/pull/20)

自分が C++ で解いていた。[自分のレビューコメント](https://github.com/dxxsxsxkx/leetcode/pull/20#discussion_r2703086670)

これ、Pythonでいけるのか？ -> Python で書いたら普通に Time Limit Exceeded になった。プログラミングコンテストとかでも、C++ だったら普通に全探索でもテストケースをパスできるけど、Python だったら TLE になることとかたびたびあったからなぁ。
