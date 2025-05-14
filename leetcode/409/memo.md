# Step 1

`string.ascii_letters (= string.lowercase + string.uppercase)` + fixed length arrayを用いる方法を実装した。
文字列をシンメトリーにすればよく、偶数個ある文字は等しく左右に散らせるが、奇数個ある文字は1つだけ中央に置いても良い。この奇数個ある文字を1つだけ中央に置く、という条件が簡潔に書けず、やや複雑になってしまった。

拡張性のために`dict` (`defaultdict`, `Counter`)を用いる方法も考えたが、先に条件分岐をきれいにすることを考えたいので一旦スキップ。

# Step 2

[Kitaken0107さんのPR](https://github.com/Kitaken0107/GrindEasy/pull/27)
	- `+= val if val % 2 else val - 1`の代わりに`+= 2 * (val // 2)`という書き方は思いつかなかった。 
	- Longest Palindromic Substringを線型時間で求めるManacher’s Algorithmというものがあるらしい。今回の問題設定では使用できないが、LeetCode 5. Longest Palindromic Substring を後で見てみようかと思う。
	- そうか、最後の最後で、奇数のものがあったら+1、なかったらそのまま途中経過を返せばいいのか。そうすればfor文の中の条件分岐が一つ減らせる。
[NobukiFukuiさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/31)
