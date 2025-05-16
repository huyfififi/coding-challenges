# Step 1

`string.ascii_letters (= string.ascii_lowercase + string.ascii_uppercase)` + fixed length arrayを用いる方法を実装した。
文字列をシンメトリーにすればよく、偶数個ある文字は等しく左右に散らせるが、奇数個ある文字は1つだけ中央に置いても良い。この奇数個ある文字を1つだけ中央に置く、という条件が簡潔に書けず、やや複雑になってしまった。

拡張性のために`dict` (`defaultdict`, `Counter`)を用いる方法も考えたが、先に条件分岐をきれいにすることを考えたいので一旦スキップ。

# Step 2

## 先駆者の方々

[Kitaken0107さんのPR](https://github.com/Kitaken0107/GrindEasy/pull/27)
	- `+= val if val % 2 else val - 1`の代わりに`+= 2 * (val // 2)`という書き方は思いつかなかった。 
	- Longest Palindromic Substringを線型時間で求めるManacher’s Algorithmというものがあるらしい。今回の問題設定では使用できないが、LeetCode 5. Longest Palindromic Substring を後で見てみようかと思う。
	- そうか、最後の最後で、奇数のものがあったら+1、なかったらそのまま途中経過を返せばいいのか。そうすればfor文の中の条件分岐が一つ減らせる。
[NobukiFukuiさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/31)

お二方のように、`is_odd_added`のようなフラグで+1する操作を最後に回せば綺麗に書けそう。

## Solutions on LeetCode

[https://leetcode.com/problems/longest-palindrome/solutions/6642768/unlock-palindrome-frequency-tricks-to-build-the-longest-one-possible](https://leetcode.com/problems/longest-palindrome/solutions/6642768/unlock-palindrome-frequency-tricks-to-build-the-longest-one-possible)
	- 「奇数があるか」という情報に対して、フラグを持つ代わりに、もし奇数の文字があったら出来上がった回文の長さが入力で与えられた文字列の長さより小さくなる、ということを使用している。

[https://leetcode.com/problems/longest-palindrome/solutions/5255173/faster-less-mem-detailed-approach-set-approach-python-java-c](https://leetcode.com/problems/longest-palindrome/solutions/5255173/faster-less-mem-detailed-approach-set-approach-python-java-c)
	- ループを2回回す代わりに、1回だけ文字列をチェックしていく。`set`に入れていって、2個見つかり次第、回文の長さとして足していく。

LeetCodeに載っている解法は驚きと発見を与えてくれるが、誰もが思いつくような解法を安定して出力できるようになりたい気持ちが強いので、一旦これらの解法は脳内の隅に留めるくらいにしておく。

## 迷ったところ

回文の長さを保持する変数名をどうしようかと思った。`max_len`は、確かに最終的に最大の長さになるが途中経過ではmaxではないような、`palindrome_length`は主観的にやや長いな、と思うような。

# Feedback

```python
palindrome_length += count // 2 * 2
has_odd_count |= count % 2 == 1
```

などとして、条件分岐を減らす方がわかりやすいかもしれない。

他のバリエーションとして、演算子の優先順位で読み手を混乱させないために `(count // 2) * 2`, `|=`はわかりづらいので素直に`bool`をif文で扱うことも考えて良さそう。
