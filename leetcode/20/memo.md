# step 1

- approach 1: Remove valid bracket pairs one by one
	- Time complexity: O(n^3)
		- 1. Each step removes 2 brackets.
		- 2. We iterate through the entire string for each step.
		- 3. String concatenation involves copying, which adds overhead.
	- Space complexity: O(n^2) (I'm not very confident)
		- Call stack usage: O(n), since we can have up to n/2 recursive calls.
		- Each recursive calls create a new string: O(n) space per call.
		- Therefore, the cumulative space could reach O(n^2)
- approach 2. Use a stack to match brackets (knowledge)
	- Time complexity: O(n), as we scan the string once.
	- Space complexity: O(n), since at most `n` brackets will be stored on the stack.

# step 2

- Since Python dictionaries are mutable, naming a local dictionary `BRACKET_PAIRS` in all caps might be misleading, as all-caps typically implies a global constant.
- Use early `return` or `continue` statements to reduce nesting and improve readability (?) in Python code.

[saagchickenのpull request](https://github.com/saagchicken/coding_practice/pull/21/files)を眺めて、だいたい同じような解法であることを確認。

↑のプルリクエスト上のコメントで、PEP8にempty sequences は falseであることを利用せよ、との記載があることに気づく。PEP8は定期的に眺めるようにしているし、既にこのパターンには従えていたが、意外と見落としているスタイリングフォーマットがあるのかもしれない。TODO: PEP8で今まであまり意識していなかったセクションを見直してみる。

```
# Correct:
if not seq:
if seq:
```

```
# Wrong:
if len(seq):
if not len(seq):
```

との例示があるが、len(seq)をintと比較する例がどちらに属するのか明示されていないのでややわかりづらいなと思った。軽くGoogleしたところ、if not seqがpythonicがPythonicな書き方であることは理解しつつlen(seq) == 0の方がわかりやすいと主張する人たちも少なからず存在していたので趣味の範囲かなとも思った。

bracket\_map -> open\_to\_close もなるほどと思ったが、もう少しいろんな人のコードを見て多くの人はどちらの方がわかりやすく感じるか確認する必要があると思った。ある程度趣味の範囲内？なのかなとも思う。

# step 3
