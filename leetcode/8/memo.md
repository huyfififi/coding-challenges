# Step 1

方針はすぐに立ったものの、問題文を読んだだけでは想像しなかったパターンの入力 (-+10 とか) でかなり引っかかってしまった。そして、それらに対応するために条件分岐が複雑になってしまった。
この問題のAcceptance Rate が 20% と著しく低く、Discussionを覗いてもみんな同じような引っ掛かりを経験しているようなので、私もある程度のケースの見落としは許容されると思いたい。
もちろん問題文を読んでサンプルに挙げられていないケースまで想像が及ぶことがベストなのだが...。

また、直接 `std::atoi` は用いていないものの、面接官が求めている解き方をしていないかもしれないという不安がある。

# Step 2

ざっと過去のPRを眺めた感じ、主なポイントは以下の二点。

## オーバーフロー対策

Step 1 では、途中結果をオーバーフローさせないために `long long` で一旦計算する方針をとっていたのだが、

[Satorien さんのPR](https://github.com/Satorien/LeetCode/pull/58/changes#diff-6360db6e2a790c155563f693493e79f9fdbe0bcac7ddbf5fe63c39382745bd7bR51)

```python
if sign == POSITIVE and (MAX_INT - int(s[index])) // 10 - num < 0:
```

なるほど、`num * 10 + digit > MAX_INT` という不等式を式変形すればオーバーフローさせずにチェックできるのか。

## char -> int

[potrue さんのPR](https://github.com/potrue/leetcode/pull/59/changes#diff-7a9f34375367e42ff3beedb19cca413cb336443e19c2f8bcd5ebb565e15458f1R199)

```cpp
int digit = *it - '0';
```

私のStep 1のようにわざわざstringを舐めなくても、こうすれば簡潔に decimal の char を integer に変換できそうだ。
また、テストケースはパスしているが、私のStep 1は `*it != s..end()` のチェック (`start < s.size()`) をしておらず、入力によっては undefined behavior になってしまうことに気がついた。

[Chromium Code Search - "digits - '0'"](https://source.chromium.org/search?q=%22digit%20-%20%270%27%22&ss=chromium&start=1)

`digits - '0'`は結構出てくるパターンっぽい。

また、[std::isdigit](https://en.cppreference.com/w/cpp/string/byte/isdigit.html)や[std::isspace](https://en.cppreference.com/w/cpp/string/byte/isspace.html)を使えば簡潔に、また自前の処理がバグを起こすことを心配する必要なく書けそう。
Pythonは仕事で使っているので定期的にドキュメントを見て、どういう関数があるのかチェックしているのだが、他の言語ともなるとなかなか難しいな。

# Step 4

メモ

`((max_int - digit) / 10)` は整数除算で少数部分が切り捨てられるが、比較している `integer` は整数なので、`integer > floor((max_int - digit) / 10)` と同じ。
