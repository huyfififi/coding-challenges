# Step 1

色々考えてみたが、思いついた解法が一つだけだったのでとりあえず実装した。テストケースが 48/49 パスした。

先頭から舐めていくが、カッコが出てきたら対応する右側の閉じカッコを探してきて、その部分を抜き出して再帰的に処理する。

問題はカッコが深い入れ子になっている場合で、例えば

```
((6)) -> (6) -> 6
```

と、カッコの数だけ再帰が発生することにある。再帰が O(N)、対応するカッコを探してくる操作で O(N) 合計で O(N^2) になり、制約が

> 1 <= s.length <= 3 * 10^5

なので、O(N^2) だと大体 10 ^ 11 steps 必要になる。これは LeetCode の設定上 (Python で大体 10 ^ 5 s かかるのを考えても) 時間がかかりすぎる解法なのだろう。

## AI に相談

いつも通り、AI にヒントを小出しにしてもらって、方針が立てられた。LeetCode 20\. Valid Parentheses を思い出せば、stack を使用すると良い感じにカッコ対応を処理できる。

普通に左から右に舐めていって、開きカッコに遭遇したら Stack に途中結果を push し、閉じカッコが来たら カッコ内の結果と最後の途中結果を足し合わせればいけそう。positive/negative の sign をどう処理するかは... 他の stack を持つかどうか、うまく思考がまとまらないので、とりあえず書いてみよう。

# Step 2

## AI

### Sign enum の是非

sign を +1 と -1 で表現すれば、if 文をわざわざ書かなくても (`if sign == Sign.POSITIVE:` のようなことをしなくても) よくなるからオススメだとされた。sign という変数に意味を持たせすぎるような気がして避けたが、そちらの方がコードが単純になりそうだな。

### Stack の管理

別々に `results` stack と `signs` stack を持つより、同時にpush/pop される意味的に繋がりがある値なので一緒に持つといいとオススメされた。

## LeetCode Solutions

[https://leetcode.com/problems/basic-calculator/solutions/7576826/most-optimal-beats-100-all-languages-sta-jd4n/](https://leetcode.com/problems/basic-calculator/solutions/7576826/most-optimal-beats-100-all-languages-sta-jd4n/)

数字だった場合に繰り返し `result = result * 10 + int(c)` する操作を最初に持ってくれば、自前で ループ変数を管理せず `for c in s:` で扱えている。

[str.isdigit()](https://docs.python.org/3/builtins/stdtypes.html#str.isdigit) のことを完全に失念していた。わざわざ `if c in string.ascii_lowercase` のようなことをしなくてもよかったな。

[https://github.com/python/cpython/blob/c6c060843b7635b5a1f82e0983d803eb0d185b5d/Lib/curses/ascii.py#L66](https://github.com/python/cpython/blob/c6c060843b7635b5a1f82e0983d803eb0d185b5d/Lib/curses/ascii.py#L66)

`ord()` の返す値の範囲で判定していそう。計算量的には `in string.ascii_lowercase` と同じだと思うが、必要な操作が少ない。

# Step 4

## Recursive-Descent Parsing

[https://www.cs.rochester.edu/u/nelson/courses/csc\_173/grammars/parsing.html](https://www.cs.rochester.edu/u/nelson/courses/csc_173/grammars/parsing.html)

ざっと目を通して、よくわからなかったが、例として `1 + (2 * 3) / 4` が挙げられており、問題設定がそのままなので、この問題は recursive descent parser が念頭にあっての問題なのかもなと思った。

AI に色々質問したが、理解にもう少し時間がかかりそう。日常使いとは違う "grammar" という用語があるよう。
