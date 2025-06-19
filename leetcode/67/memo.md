# Step 1

## `int()`の第二引数、`bin()`を利用する方法

`int()`の第二引数に基数を指定できることを知っていたので、それを利用する方法が最初に思いついた。コーディングインタビューだともっと実装力をみたいと思うので、こちらは想定解ではないだろうと予想する。

```
In [1]: int("10")
Out[1]: 10

In [2]: int("10", 10)
Out[2]: 10

In [3]: int("10", 2)
Out[3]: 2
```

```
In [1]: bin(2)
Out[1]: '0b10'
```

## 愚直に足し算・繰り上がりを実装する方法

数学で習った通り、二進数（のみならず他の基数にも対応）の足し算を実装。
実装自体はすんなりできたが、`answer`・`digit`という変数名、特に`digit`は名前と中身が一致していないな、と思ったが他に良い案が思いつかなかった。他の方々の命名を眺めてみることにする。

# Step 2

## 他の方々のコードを見てみる

Discordで検索をかけても、一人しか過去に解いた方が見つからなかった。

[NobukiFukuiさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/35)
- ある桁の足し算の合計には`total`が良さそうだ。LeetCodeのAdd Two NumbersのSolutionsを眺めても`total`としていて、他にいい案は思いつかない。
- `int`に変換しないでそのまま扱う方法は思いつかなかったな。

Linked Listで似たようなことをやる[LeetCode 2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/)の方は新井さんの問題集の方にあるので前例が豊富そう。少し眺めてみる。

- [JikuharaさんのPR](https://github.com/Jikuhara/LeetCode/pull/11)
- [nktr-cpさんのPR](https://github.com/nktr-cp/leetcode/pull/6)
- [mptommyさんのPR](https://github.com/mptommy/coding-practice/pull/5)
- [maeken4さんのPR](https://github.com/maeken4/Arai60/pull/5)
- [skypenguinsさんのPR](https://github.com/skypenguins/coding-practice/pull/2)

Add Two Numbersの解法を真似ると、このような形になるだろうか。

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = list(a)
        b = list(b)
        carry = 0
        answer = []

        while a or b or carry:  # while a_i >= 0 or b_i >= 0 or carry == 1 として使用スペースを少なく抑える方法もあり
            total = carry
            if a:
                total += int(a.pop())
            if b:
                total += int(b.pop())

            answer.append(str(total % 2))
            carry = total // 2

        return "".join(answer[::-1])
```

確かに、書いてみると納得感がある。また、LeetCodeのAdd BinaryのSolutionsをざっと見ても、ほとんどこの解法だ。
私は、自分の回答であるバイアスは意識しつつ、私の`step1_bin_addition.py`の方がわかりやすく感じる。なぜなら条件分岐・ループ条件が少なく抑えられていて処理を追いやすいので (脳内フローチャートがシンプル)。
他の方々の意見も伺いたいところです。

## その他

### `issubclass(bool, int)`

少し時間をおいてみて、そういえば`bool`は`int`のsubclassで、`True`と`False`は内部的に`1`と`0`なので、いちいち`int(a[i])`と変換しなくても良いのか、と気づいた。が、一般的な知識ではないと感じるし、`bool`型と`int`型を混ぜて扱うことに、バグを起こすのではないかという不安を抱えるのでやめておく。

```
In [1]: issubclass(bool, int)
Out[1]: True

In [2]: total = True + True + 1

In [3]: total
Out[3]: 3
```

### `reversed()` and `rjust()`

`reversed()`と`rjust()`の存在をstep 1の段階で忘れていた。`[::-1]`でリストをひっくり返したり、`"0" * n`で文字列を繰り返したりするのは、Pythonを普段扱わない方には自明ではないだろうと思うので、`reversed()`や`rjust()`の方が関数名から処理を推定しやすくていいかな、と考えた。

### `itertools.zip_longest()`

ChatGPTとやりとりしていたら、`zip_longest`を提案された。そういえばFluent Pythonの助けもあり一回は`itertools`に目を通した記憶があり、読むのには困らないが、自分でコードを書く上では思いつきづらい。過去一緒に働いたことのある方々を思い出すと、チームによって好ましく思うかどうか分かれそうだが、偏ったサンプルかもしれない。

```python
from itertools import zip_longest


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        answer: list[str] = []
        carry = 0
        for digit_a, digit_b in zip_longest(reversed(a), reversed(b), fillvalue="0"):
            total = int(digit_a) + int(digit_b) + carry
            answer.append(str(total % 2))
            carry = total // 2

        if carry == 1:
            answer.append("1")
        return "".join(reversed(answer))
```

TODO: Step 3
TODO: Are there any differences between reversed() and [::-1]?
