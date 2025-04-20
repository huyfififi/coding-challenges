# Step 1

副作用がない形にすると `image`をコピーしないといけないので時間・計算ともに O(m * n)かかってしまう。副作用があってもいい、と仮定しておく。

事前に指摘されていたので、queueやcall stackに積む数を減らすために、新しい要素をqueue・call stackに入れる前に`visited`のフラグを立てておく（今回の場合色を先に塗り替えておく）ことを心がけた。

上下左右のマスに移動する条件分岐がやや見辛いが、改善案は思いつかなかった。

後から考えたら、`m` -> `height`, `n` -> `width`とした方が、変数が何を意味するのかわかりやすくなるかなと思ったが、`m`、`n`も`i`、`j`同様に広く使われているから気にしすぎなのか、とも考えた。

# Step 2

[NobukiFukuiさん](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/15)
	- 範囲チェックを呼び出し後にやる方法もある。
	- directionを示すリストを作ってループを回す方法は、if文を並べるのとどっちが人気なのだろうか。
	- `nrows`, `ncols` (number of rows, number of cols)という変数の命名、わかりやすいなと思った。
