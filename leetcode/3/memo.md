# Step 1

解法を思いつくまで約25分、テストケースをパスする解答を書き終えるまで約40分かかった。

最初に、`seen`という`set`を用いて何とかできないか、と考えたが、`set`では文字の位置情報を失ってしまうのでうまくいかないなと思った。
次に、何とか再帰的な関係を見出して動的計画法に持ち込めないか考えてみたが、テキトーに問題を分割してみても、結局被ってしまう文字同士の位置関係をどうにかして処理しないといけないので、筋が悪そうだと感じた。

少しパニックになりかけていたのを感じたので、一旦落ち着いて、自分が脳内で問題を解く (手作業で解く) ならどうするか考えてみた (後から考えると、これを最初にやるべきだった)。

"abcabcbb" を先頭から眺めて i = 3 の "a" にたどり着いたとき、i = 0 の "a" を捨てて、i = 1 の "b" から始まる文字列を考えればいいな。また、i = 4 の "b" に進んだときは、i = 1 の "b" を捨ててその次からなる部分文字列を考えればいい。 -> (もう少し問題で挙げられている例を考えてみて) -> 既に出会った文字に遭遇した場合、前に出会った場所の位置情報があればいいのか。`set`ではなく`dict`を使用するべきだったんだな、と気づいた。-> `step1.py`

`step1.py`を書いてから少し時間をおいてみて、これ、大学時代に競プロ (特に熱心にやっていたわけではないが) で出会ったしゃくとり法と同じだな、と気づいた。

[Qiita - drken - しゃくとり法 (尺取り法) の解説と、それを用いる問題のまとめ](https://qiita.com/drken/items/ecd1a472d3a0e7db8dce)

> しゃくとり法は、以下の形式の問題を解くときに使える可能性のあるテクニックです:
> 長さnの数列a_1, a_2, ..., a_nにおいて
> - 「条件」を満たす区間 (連続する部分列) のうち、最小の長さを求めよ
> - 「条件」を満たす区間 (連続する部分列) のうち、最大の長さを求めよ
> - 「条件」を満たす区間 (連続する部分列) を数え上げよ

[AtCoder Beginner Contest 229 D - Longest X 解説 by sugarrr](https://atcoder.jp/contests/abc229/editorial/2956?lang=ja)

> 尺取り法とは端的に言うと、区間の左端と右端を尺取り虫のように動かすことで、条件を満たす区間を高速に見つける、というアルゴリズムです。

そう考えると、`dict`の代わりに`set`を用いても、条件を満たさない場合に左のポインタを動かし続けるということをすれば、解答が書ける。 -> `step1_syakutori.py`

どちらにせよ、多めに見積もっても二つのポインタを先頭から末尾に動かしているだけなので、時間計算量はO(n)、空間計算量はO(1) なぜなら、出てくる文字の種類が "English letters, digits, symbols and spaces" に限られているため。

# Step 2

先駆者の方々のPRを見る

- [Kaichi-IrieさんのPR](https://github.com/Kaichi-Irie/leetcode-python/pull/9)
    - 変数の命名は若干異なるだけで、私がStep 1で行った方法とまるきり同じ。
- [TORUS0818さんのPR](https://github.com/TORUS0818/leetcode/pull/50)
    - `left_i`, `right_i`よりも`left`, `right`とする方が簡潔で読みやすいのか。私もいつも悩む点だ。Discussionがあると参考になってありがたい。
        - 私も[Odaさんに同じようなフィードバックを受けた](https://github.com/huyfififi/coding-challenges/pull/14#discussion_r2082999110)ことを思い出した。
    - 私も自分の解答を書いているとき、`start`, `end`がinclusiveなのかexclusiveなのか伝わりづらいなと思ったが、冗長になっても仕方がないので、処理から理解してもらう方がいいかなと思った。
    - 二つのポインタの命名に関して言及されていたので、リーダブルコードを確認してみたが、inclusive rangeには`first` & `last`、exclusive rangeには (C++の標準ライブラリなどで広く使われている)`begin` & `end`が良いらしい。
        - 個人的には、どのみち英語の文法的にはinclusiveかexclusiveか定まらないのだから、どちらでも、`start` & `end` でもいいような気がするのだが。
- [KentaroJayさんのPR](https://github.com/KentaroJay/Leetcode/pull/4)
    - Hungarian Notationというものがあるのか。[Joel on Software - Making Wrong Code Look Wrong](https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/) -> 元気がある時に見てみよう。
        - Joelさんのブログだと、昔[Fire And Motion](https://www.joelonsoftware.com/2002/01/06/fire-and-motion/)を読んで感銘を受けた記憶がある。(モチベーション向上は短期的にしか続かなかったが...)
    - 私の`step1_syakutori.py`でも、`s[end]`がループ内で二度アクセスされていて、大事な値なので、変数をおいた方がいいのだろうか...。
- [FuminitonさんのPR](https://github.com/Fuminiton/LeetCode/pull/50)
    - 私と同じ`start` & `end`という命名だ。
    - なるほど、入力がASCIIだとするとそれが取りうる値の分だけリストを用意すればいいのか。
- [ryosuketcさんのPR](https://github.com/ryosuketc/leetcode_arai60/pull/37)
    - 私も、左のポインタを右にしか動かしてはいけないはずが、左に動かしてしまってエラーになった。この問題の低いAcceptance Rateは、ここにあるのかな。

みなさん初見ですんなり解けているのすごいなぁ。
