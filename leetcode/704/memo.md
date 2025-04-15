# Step 1

案の定while文の条件でつまづいた。どこかで始まりは含み・終わりは含まない半開区間にしておくと便利、Pythonのlistもそうなっている、というのを目にした記憶があり、なんとなくBinary Searchも半開区間 (`left_i = 0`, `right_i = len(nums)`)で実装していた。しかし、Pythonのlistのように区間を連結させるわけでもないし、`left_i == right_i (== middle_i)`の次でループから抜けることが想像しやすいので、閉区間での表現の方が私には理解しやすく感じた。

# Step 2

- [kzhra-san](https://github.com/kzhra/Grind41/pull/9)
	- [nodchipさんTweet](https://x.com/nodchip/status/1765579286646530148)
		- 約2/3の人が、ループの方が末尾再帰よりも読みやすいと投票している。母集団が偏っている可能性はあるにせよ、逆に約1/3の人が末尾再帰の方を好むのは面白い。
	- C++の`lower_bound()`の実装を調べられている。
