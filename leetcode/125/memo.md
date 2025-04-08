# Step 1

## Solution a

問題文の通り、大文字を小文字に変換し、アルファベット・数字以外の文字を除外した文字列を反対から読んでも同じかどうか確認する方法。

Time Complexity: O(n)
Space Complexity: O(n)

### 引っかかった・悩んだ点

- `str.isalnum()`を思い出すのに少し時間がかかった（脳内で即座に取り出せる場所になかった）。
- `chars_to_validate`という変数名をもっと端的なものにできないか？
	- `normalized_chars`? `filtered_chars`は、私の解法の場合大文字->小文字変換もしているのでfilterだけではないような気がして避けた。
- そもそも素直に問題文通りの処理を書き、`chars_to_validate`を保持しなくても、両端からポインタを動かしてチェックできるのでは？
- Valid ParenthesesのようにStackで解けないか？ -> Valid Parenthesesとの違いは、回文では必ずしも全ての要素が対応するわけではない（真ん中に一文字残る場合も回文）。
- recursiveな解法でも解けるが、alphanumeric以外を無視する操作を考えると、また新しいstringを作ってしまうとその分memory spaceが必要になるのでそれを避けると、綺麗には書けない

## Solution b

両端から、[アルファベットまたは数字]以外の文字を無視して、全ての文字の対応（真ん中に一文字残るのも許容）が確認できれば回文。

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
