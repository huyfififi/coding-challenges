# Step 1

レビュー依頼をされた時に一度解いたことがあったような気がするのだが、内容を忘れていた。いかんせんLeetCode練習会をやり始めてから一年以上経過してしまったので、ある程度仕方がないか。理想を言えば、もっと早足で駆け抜けられたらよかったのだろう。

ChatGPT にヒントをもらった。3回くらいヒントを小出しにしてもらってやっと解答に辿り着いた。-> `step1.py`

> Minimal direction: think about whether you really need to compare every pair of words to discover which words are neighbors.

> “What possible neighbor words can I generate from this word?”

> 25 × 10 = 250 — every string exactly one character away from one 10-character word.

チェック・ループするものを工夫して入れ替える問題にこの前も出会ったような気がするが、記憶がない。類題を出されてすぐに解答に辿り着ける自信はまだないが、頭になんとなく入れておこう。

文字列の数を N 文字列の長さを L とすると

時間計算量: queue に word は高々 1 度しか入らず、各文字列に対して、26 文字 * L positions の候補を検討するが、その時に`list()` と`.join()`を使用している (`O(L)`) ので、総じて `O(NL)`。

空間計算量: 文字列の set、queue、seen に最大で N 個の長さ L の文字列が入るので `O(NL)`
