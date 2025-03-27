# step 1

- approach 1: Remove valid bracket pairs one by one
	- Observation: In a valid bracket string, there is always at least one pair of adjacent matching brackets.
	- Time complexity: O(n^2)
		- In each step, we remove exactly two brackets. We have to scan the string (which takes O(n) time) to find an remove a valid pair.
		- Since we remove two brackets per step, we perform roughly n/2 steps. Multiplying O(n) per step by n/2 steps gives O(n^2) in total.
		- Although string concatenation also takes O(n) time, we only do it once per step, so overall the time complexity is O(n^2).
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

[saagchickenさんのpull request](https://github.com/saagchicken/coding_practice/pull/21/files)を眺めて、だいたい同じような解法であることを確認。

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

との例示があるが、len(seq)をintと比較する例がどちらに属するのか明示されていないのでややわかりづらいなと思った。軽くGoogleしたところ、if not seqがPythonicな書き方であることは理解しつつlen(seq) == 0の方がわかりやすいと主張する人たちも少なからず存在していたので趣味の範囲かなとも思った。

bracket\_map -> open\_to\_close もなるほどと思ったが、もう少しいろんな人のコードを見て多くの人はどちらの方がわかりやすく感じるか確認する必要があると思った。ある程度趣味の範囲内？なのかなとも思う。

-> 前回も同じ指摘を受けたのだった（ref: [ichika0615さんのコメント](https://github.com/huyfififi/coding-challenges/pull/1#discussion_r2002776605)）。もう一度考え直してみたところ、hash tableのkey -> valueの関係をうまく表現できているし、keyとvalueがなんなのか一目で理解できるので `x_to_y` という表現はわかりやすく感じた。次回からちゃんと気に留めて使っていこう。

# step 3

None

# Feedback

# step 4
