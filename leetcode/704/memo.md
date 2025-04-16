# Step 1

案の定while文の条件でつまづいた。どこかで、プログラミングにおいては始まりは含み・終わりは含まない半開区間にしておくと便利、Pythonのlistのスライス・range()関数などもそうなっている、というのを目にした記憶があり、なんとなくBinary Searchも半開区間 (`left_i = 0`, `right_i = len(nums)`)で実装していた。しかし、Pythonのlistのように区間を連結させるわけでもないし、`left_i == right_i (== middle_i)`の次でループから抜けることが想像しやすいので、閉区間での表現の方が私には理解しやすく感じた。
	- 遠い記憶だが、見たのはこの記事かもしれない [半開区間の魅力 〜プログラミングでのスマートな区間の扱い方〜](https://qiita.com/_ken_/items/25cede552e3e325b9ef1)

# Step 2

Grind 75をやっている方々が少ないように見受けられる。

- [kzhraさん](https://github.com/kzhra/Grind41/pull/9)
	- [nodchipさんのTweet](https://x.com/nodchip/status/1765579286646530148)
		- 約2/3の人が、ループの方が末尾再帰よりも読みやすいと投票している。サンプルが偏っている可能性はあるにせよ、逆に約1/3の人が末尾再帰の方を好むのは面白い。
	- C++の`lower_bound()`の実装を調べられている。
- [Kitaken0107さん](https://github.com/Kitaken0107/GrindEasy/pull/11)
- [colorboxさん](https://github.com/colorbox/leetcode/pull/10)
	- `right`の初期値が大きい場合`int`で表現できる範囲を超えてしまうので、それを避ける方法として`int middle = (right - left) / 2;`
- [rihibさん](https://github.com/rihib/leetcode/pull/27)

みなさん `left`, `right`, `mid`という変数名を用いていたが、`left`だけで左側のポジションを指す変数って瞬時に判断できるのかなぁという疑問を抱いた。スコープが小さいので別にいいのだろうが、個人的には`left_i`の方がarrayのindexであることがわかりやすく感じる。
	- ちょっとネットサーフィンしたら、`lo & hi`や`start & end`という書き方もある :thinking\_face:

`step2.py` -> この場合`_binary_search()`は`search()`の中でしか使われないので引数から`nums`を省いた方がouter functionから来ていることが明確。

Step 1と大きく変わらなかった。

# Step 3

Step 2と大きく変わらなかった。
