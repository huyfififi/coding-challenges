# Step 1

[LeetCode 57\. Insert Interval](https://leetcode.com/problems/insert-interval/description/) が似たような問題、というか若干入力のフォーマットが違うだけでほぼ同じだなと思った。
それ以外は特に何も思わなかった。

# Step 2

Step 1 をしている時、変数名がしっくりこないな〜と思っていたが、今見ているintervalを単に`interval`、一つ前のmerge途中であるintervalを`last_interval`とするのが一番良く思えた
それでも完全にしっくりと意味と名前を対応させられている感じはなんだかしないのだが。
Step 1 は説明的であることを心がけたが、読まなければいけない行数が多いので逆に読みにくいかもしれない。

`std::vector<std::vector<int>> sorted_intervals(intervals);`の時点では厳密にはソートされていないので名前とのチグハグ感があるが、他に良い案も思いつかなかった。ソートするまでの処理と、続く処理の間に一行空行を挟んでいるので誤解はないと思うが。
