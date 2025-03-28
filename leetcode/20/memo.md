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

- "Never use the characters ‘l’ (lowercase letter el), ‘O’ (uppercase letter oh), or ‘I’ (uppercase letter eye) as single character variable names." [PEP8 - Names to Avoid](https://peps.python.org/pep-0008/)
	- PEP8について指摘されることが多いので、TODO: 次回までにPEP8を一度は流し見する・`ruff`/`flake8`の徹底
		- (普段の開発においては、個人的には`black`も使用し、diffを見比べるようにしている。)
- **rope (or cord)**という、文字列へのinsertions, deletions, and concatenationsが効率的に行えるdata structureがある。これは発展的な知識だが、存在自体は気に留めておいても損はないと思うので記憶しておく。
- 基本的にはスタイルガイド (PythonにおけるPEP8) に従っておく。そこに至った合理性があるはずなので。時と場合に応じて臨機応変に対応する姿勢も忘れずに。 [ref](https://docs.google.com/document/d/11HV35ADPo9QxJOpJQ24FcZvtvioli770WWdZZDaLOfg/edit?tab=t.0#heading=h.9xjrags8izok)
- [str.startswith()](https://docs.python.org/3/library/stdtypes.html#str.startswith)はtupleを引数に取ることができる
	- "Return True if string starts with the *prefix*, otherwise return False. *prefix* can also be a tuple of prefixes to look for."
	- ちょっと実装が気になってCPythonのGitHub repositoryを覗いてみたが現在の私の理解力の範疇を超えていた。今度リトライ。

---

次回（も）気をつけようと思うこと

- TODO: PEP8流し見・徹底
- `key_to_value`という`dict`の命名アプローチ
- 1行の情報量は少なく
- return early
