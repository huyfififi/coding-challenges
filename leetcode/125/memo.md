# Step 1

## Solution a

問題文の通り、大文字を小文字に変換し、アルファベット・数字以外の文字を除外した文字列を、反対から読んでも同じかどうか確認する方法。

Time Complexity: O(n)
Space Complexity: O(n)

### 引っかかった・悩んだ点

- `str.isalnum()`を思い出すのに少し時間がかかった（脳内で即座に取り出せる場所になかった）。
- `chars_to_validate`という変数名をもっと端的なものにできないか？
	- `normalized_chars`? `filtered_chars`は、私の解法の場合大文字->小文字変換もしているのでfilterだけではないような気がして避けた。
- そもそも素直に問題文通りの処理を書き、`chars_to_validate`を保持しなくても、両端からポインタを動かしてチェックできるのでは？ -> 2つ目の解法
	- Two pointersの解法だと行数がある程度ありtypoしがち・何をしているかパッと見ではわからない・ポインタの動きを脳内で想像しないといけないのでやや負荷がかかる。
		- 入力文字列がメモリに対して十分に小さいことが確認できるなら、Two pointersの解法は避けたいな、と感じた。
- recursiveな解法も書くことができるが、alphanumeric以外を無視する操作を考えると、また新しいstringを作ってしまうとその分memory spaceが必要になるのでそれを避けると、綺麗には書けない
- 一行が持つ情報が多くなるのでlist comprehension避けたが、これくらいの複雑さならlist comprehensionの方が、個人的にはわかりやすく感じた。

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        normalized_chars = [c.lower() for c in s if c.isalnum()]
        return normalized_chars == normalized_chars[::-1]
```

## Solution b

両端から、[アルファベットまたは数字]以外の文字を無視して、全ての文字の対応（真ん中に一文字残るのも許容）が確認できれば回文。

Time Complexity: O(n)
Space Complexity: O(1)

# Step 2

- [t-ookaさん](https://github.com/t-ooka/leetcode/pull/6)
- [kzhraさん](https://github.com/kzhra/Grind41/pull/5)
	- `left`, `right`, early return
- [Kitaken0107さん](https://github.com/Kitaken0107/GrindEasy/pull/8)
	- alphanumericの判定に[ord(c)](https://docs.python.org/3/library/functions.html#ord)を使用していた。一応意識しておこう。
- [colorboxさん](https://github.com/colorbox/leetcode/pull/7)
- [hayashi-ayさん](https://github.com/hayashi-ay/leetcode/pull/9)

`step1_b.py`と変わらなかったのでコードは省略。

# Step 3

step 1, step 2 と変わらなかったので省略。

# Feedback

[`str.isalnum()`](https://docs.python.org/3/library/stdtypes.html#str.isalnum)は`str.isalpha()`, `str.isdecimal()`, `str.isdigit()`, and `str.isnumeric()`から成り立っている。なので

```
In [1]: "四".isalnum()
Out[1]: True

In [2]: "²".isalnum()
Out[2]: True
```

というケースも`True`を返し、これは[a-Az-Z0-9]という直感に反する。ここは面接時に面接官とすり合わせを行った方がいいだろう。

---

s = re.sub(r'[^a-zA-Z0-9]', '', s)というやり方も覚えておこう。正規表現は業務でも使う頻度が高い。
