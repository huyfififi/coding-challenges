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

やりたいことはわかったけど、これって取りこぼしとかないのだろうか。ヒントを見る前にしゃくとり法みたいにできないかちょっと考えて、答えをスキップしてしまうような気がしていたが、頭の中でいくつかやってみる限り、取りこぼしはなさそう。やることは単純そうなので、書き上げるのにそこまで時間はかからないか。記憶が蘇ってくると、これ大学時代にAtCoderを齧った時に練習した、しゃくとり法まんまだな。脳内のすぐ使える位置になかったのが悔しい。-> `step1.py`

> `s` and `t` consist of uppercase and lowercase English letters.

という制約から、文字種は多くても52種で限定的とみなすと、時間計算量を考える時に文字カウンタの比較は無視しても良い。

`t`の文字カウンタの構築で`O(n)`、あとは2つのポインタを右に移動させていくだけなので`O(m)`、合計で時間計算量は `O(m + n)`。処理時間は52種の文字比較の定数も考えると大体 0.1 ~ 10 秒くらいのオーダーか。

# Step 2。

- [hayashi-ay さんのPR](https://github.com/hayashi-ay/leetcode/pull/73)
- [tom4649 さんのPR](https://github.com/tom4649/Coding/pull/127)

外側のループは右側 (substring の終わり) だけ動かしていけばスッキリ書けるのか、思い至らなかった。そこと、カウンタの上手い使い方を頭に入れれば、自分でも他の方々の step 3 に近いものが再現できそう。

TODO: なぜこのやり方でできるのか言語化してみる。

軽くGoogleした限り、尺取り法という名前がどこから来たのかはよくわからなかった。
昔この記事を読んだ記憶はある。[Qiita - しゃくとり法 (尺取り法) の解説と、それを用いる問題のまとめ by けんちょん (Otsuki)](https://qiita.com/drken/items/ecd1a472d3a0e7db8dce)
