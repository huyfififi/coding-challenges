# Step 1

`string.ascii_letters (= string.lowercase + string.uppercase)` + fixed length arrayを用いる方法を実装した。
文字列をシンメトリーにすればよく、偶数個ある文字は等しく左右に散らせるが、奇数個ある文字は1つだけ中央に置いても良い。この奇数個ある文字を1つだけ中央に置く、という条件が簡潔に書けず、やや複雑になってしまった。

拡張性のために`dict` (`defaultdict`, `Counter`)を用いる方法も考えたが、先に条件分岐をきれいにすることを考えたいので一旦スキップ。
