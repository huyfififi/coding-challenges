# Step 1

愚直にやれば、`s` の全ての substring に対して、`t` とマッチしているか判定すればいい

```py
for start in range(len(s)):
    for end in range(start + 1, len(s)):
	# convert s substring and t into counter and match
```

みたいな感じで `O(m ^ 2 * (m + n))` だろうか。制約から `1 <= m, n <= 10^5` なので、Python だと大体 `10 ^ 15 / 10 ^ 6 = 10 ^ 9 s` ほどかかってしまいそう。

各ループで文字カウントを再計算しなくても、カウントを使い回していけば `O(m ^ 2 * n)` にはできそうだが、それでも遅い。

手作業で解くとしても上手いやり方が思いつかない。ヒントを見てみる。

> Hint 1: Use two pointers to create a window of letters in s, which would have all the characters from t.

> Hint 2: Expand the right pointer until all the characters of t are covered.

> Hint 3: Once all the characters are covered, move the left pointer and ensure that all the characters are still covered to minimize the subarray size.

> Hint 4: Continue expanding the right and left pointers until you reach the end of s.

やりたいことはわかったけど、これって取りこぼしとかないのだろうか。ヒントを見る前にしゃくとり法みたいにできないかちょっと考えて、答えをスキップしてしまうような気がしていたが、頭の中でいくつかやってみる限り、取りこぼしはなさそう。やることは単純そうなので、書き上げるのにそこまで時間はかからないか。記憶が蘇ってくると、これAtCoderをやってた時に練習したしゃくとり法まんまだな。脳内のすぐ使える位置になかったのが悔しい。
