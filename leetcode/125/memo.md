# Step 1

## Solution a

問題文の通り、大文字を小文字に変換し、アルファベット・数字以外の文字を除外した文字列を反対から読んでも同じかどうか確認する方法。

Time Complexity: O(n)
Space Complexity: O(n)

### 引っかかった・悩んだ点

- `str.isalnum()`を思い出すのに少し時間がかかった（脳内で即座に取り出せる場所になかった）。
- `chars_to_validate`という変数名をもっと端的なものにできないか？
	- `normalized_chars`?
- そもそも素直に問題文通りの処理を書き、`chars_to_validate`を保持しなくても、両端からポインタを動かしてチェックできるのでは？
- Valid ParenthesesのようにStackで解けないか？ -> Valid Parenthesesとの違いは、回文では必ずしも全ての要素が対応するわけではない（真ん中に一文字残る場合も回文）。
- recursiveな解法でも解けるが、alphanumeric以外を無視する操作を考えると、また新しいstringを作ってしまうとその分memory spaceが必要になるのでそれを避けると、綺麗には書けない

## Solution b

両端から、[アルファベットまたは数字]以外の文字を無視して、全ての文字の対応（真ん中に一文字残るのも許容）が確認できれば回文。
