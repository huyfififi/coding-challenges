# Step 1

`n`をnodeの個数、`h`を木の高さ、`w`を木の最大幅とする。

- DFS
	- Time Complexity: O(n) (n 個の node に訪問するため)
	- Space Complexity: O(h) (call stack に積まれる最大量)
- BFS
	- Time Complexity: O(n) (n 個の node に訪問するため)
	- Space Complexity: O(w) (木の最大幅分のノードがqueueに入るため)

# Step 2

[rihib-san](https://github.com/rihib/leetcode/pull/26)
	- recursive (DFS) な解法はfunction callがcall stackに積まれていくので、iterativeにDFSを実装するとcall stackを模してstackを使用することになる。(BFSならFIFOのqueue。)
[2f9a5m75-san](https://github.com/wf9a5m75/leetcode3/pull/13)
	- rihibさんと同様、stackの中に`None`を入れないように条件を書いていた。私は条件分岐をシンプルにするためにstackの中に`None`を入れることを許容したが、それを避けたいと感じる人が多いという発見があった。
		- が、条件分岐をなるたけ減らしたい方々もおり、明確な優劣は議論されていなかったので趣味の範囲だと思われる。
	- (信頼度の高い文献は限られたリサーチ時間の中では見つからなかったが、) stack overflowとは再帰関数の呼び出しによりcall stackが溢れる状態を指し、単にstackが最大の要素数を超える場合を指すわけではないよう。
[kzhra-san](https://github.com/kzhra/Grind41/pull/6)
[colorbox-san](https://github.com/colorbox/leetcode/pull/8)
[Kitaken0107-san](https://github.com/Kitaken0107/GrindEasy/pull/9)
	- 私も最初左右のreferencesをswapさせる際、古くから使われている（と記憶している）一時的な変数をおくことを考えたが、PRを見ると`a, b = b, a`という表記はわかりやすく、値を待避させるだけの変数を省けるので、積極的に使って良いとの印象を受けた。
