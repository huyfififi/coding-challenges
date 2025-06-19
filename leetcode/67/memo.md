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

[`reversed()`](https://docs.python.org/3/library/functions.html#reversed)は`iterator`を返すので、新しいリストを返す`l[::-1]`よりも、一つ一つの値にアクセスしていく場合などでメモリ使用量が少なく抑えられる。

### `itertools.zip_longest()`

ChatGPTとやりとりしていたら、`zip_longest`を提案された。そういえばFluent Pythonの助けもあり一回は`itertools`に目を通した記憶があり、読むのには困らないが、自分でコードを書く上では思いつきづらい。過去一緒に働いたことのある方々を思い出すと、チームによって好ましく思うかどうか分かれそうだが、偏ったサンプルである可能性は否定できない。

### negative indices

Pythonは負のインデックスをサポートしているので、`step1_padding.py`のループは

```
for i in range(len(a)):
    total = int(a[-(i+1)]) + int(b[-(i+1)]) + carry
```

ともできるな、と思ったが、特に読みやすさに差がないように思える。range()の中身はシンプルになったが、0-indexedの普通のインデックスに対して、負のインデックスは後ろから1-indexedなのでやや混乱するように感じるし、カッコが多くなって対応が見辛くなってしまっている気がする。

### `divmod()`

[divmod()](https://docs.python.org/3/library/functions.html#divmod)という関数があることを初めて知った。今までの人生で出会ったことがないが、この使用を他の方々はどう思うんだろう。少し驚いてドキュメントを確認する手間が入る思うのだけれど...

```python
for digit_a, digit_b in zip_longest(reversed(a), reversed(b), fillvalue="0"):
    carry, bit = divmod(int(digit_a) + int(digit_b) + carry, 2)
    answer.append(str(bit))
```

TODO: Step 3
