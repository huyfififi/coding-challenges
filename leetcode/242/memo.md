# Step 1

len(s)をn、len(t)をmとすると

- 解法1. 入力文字列をソートして比較
	- Time Complexity: O(nlogn + mlogm) (各文字列もソートするため)
	- Space Complexity: O(n + m) (ソートによって新しい文字列を作成するため)
- 解法2. Arrayに各文字の個数をカウントして比較
	- Time Complexity: O(n + m) (1回ずつ文字列を走査するため)
	- Space Complexity: O(1) (配列のサイズはアルファベット26文字で固定のため)
- 解法3. Hash Tableで各文字の個数をカウントして比較
	- 解法2では入力にlowercaseのalphabetを想定しているが、文字一般をサポートすることができない。
	- Time Complexity: O(n + m) (1回ずつ文字列を走査するため)
	- Space Complexity: O(n + m) (ユニークな文字が最大でn + m種類ある場合)

len(s)とlen(t)が異なる場合にすぐ`return False`することで、time/space complexityのbest caseをO(1)にできる。暗黙でlen(s) == len(t)である可能性もあり、step 1では行数を減らすことを優先したが。

2重ループで各文字の個数を比較するやり方なら空間計算量をO(1)に抑えられるが、個数のmapを作って比較する方がわかりやすく感じる。

# Step 2

- [colorbox-san](https://github.com/colorbox/leetcode/pull/9)
	- `s`と`t`で別々の`dict`を持つのではなく、同じ`dict`に対して`s`の文字は`+1`、`t`の文字は`-1`し、最後に全てのkeyのvalueが`0`であることを確認する方法。これならメモリ空間の使用量を削減できる。
- [NobukiFukui-san](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/21)
	- `count()`を使うのは思いつかなかった。count()は文字列を最初から最後まで走査しないといけないので、`for c in set(s): if s.count(c) != t.count(c)`の方法は時間計算量 O(n^2)かかりそう。 
- [kzhra-san](https://github.com/kzhra/Grind41/pull/8)
	- colorbox-sanと同じくmapを一つだけ持つ方法。
- [rihib-san](https://github.com/rihib/leetcode/pull/5)
	- mapを別々に持って比較する方が素直ではないか、という指摘。
	- あまり深く考えていなかったが、文字コードの処理には落とし穴が多いようだ。

```
In [1]: "café"
Out[1]: 'café'

In [2]: "cafe\u0301"
Out[2]: 'café'

In [3]: "café" == "cafe\u0301"
Out[3]: False
```
	- 同じ文字でもUnicodeでは複数の表現を持つ場合があり、こうした場合 Unicode 正規化を行うといいらしい。
	- [unicode.normalize](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize)
- [azriel1rf-san](https://github.com/azriel1rf/leetcode-prep/pull/2)
	- `collections.Counter`を使った手法
	- [GoogleのStyle Guide](https://google.github.io/styleguide/pyguide.html#316-naming)で"Avoid abbreviation."とされているのは知らなかった。`count`を`cnt`としているコードをよく見かけるが、省ける文字数もそこまで大きくなく、普通に省略せず書いた方がわかりやすい、というのは私も同意見である。

Unicode 正規化には‘NFC’, ‘NFKC’, ‘NFD’, and ‘NFKD’の方式があるよう。詳しく調べるとかなり時間がかかりそうなので一旦スキップ。

```python
s = unicodedata.normalize("NFKC", s)
t = unicodedata.normalize("NFKC", t)
return Counter(s) == Counter(t)
```

# Step 3

`step2_collections_counter.py`と変わらなかったのでコードは省略。
