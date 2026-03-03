# Step 1

何となく最初に思ったのは、Coin Change みたいに動的計画法でできないか、ということだった。
しかし、頭の中で木を思い浮かべてもうまく再帰的な関係に落とし込めなかったので、15分の時間制限をかけてやってみていたこともあり、とにかく実装できそうな素直に木/全てのパターンを試していく方法を書いた。(-> `step1_tle.py`)
この方法を書く前に考えた実行時間は

stackに積まれうるインデックス 300 種 * wordの数 1000 個 * wordの長さ 20 = 6 * 10^6 で、C++が1秒間に10^8 (~ 10^9) 回の処理を行えるとすると、6 * 10^6 / 10^8 s = 60 ms

で実行時間的に問題ないと考えていた。
しかしながら、後から気づいたのだが、複数のパスによりstackに同じインデックスが複数積まれうるので、stackに積まれるインデックスはuniqueでwhile文の部分が最大300回、という考えが誤っていた。

少し考えて、（うまくこの時の感覚を言語化できないが）これはわざわざstackを用いなくても少し変形して普通にfor文を回せばいいのでは？と思い、実装したら全てのテストケースをパスした。(-> `step1.py`)

possible(n) を n までの文字が構築可能、とおくと、Coin Change 同様 possible(n) |= possible(n - len(word)) && (s[n - len(word):n] == word) for each word で、Tabulation ができる、と考えた。

## コードで少し悩んだところ

`std::vector<bool>`は特殊化されており、パフォーマンスが落ちる可能性があるので注意、`std::vector<char>`などが代替案としてある。というフィードバックをいただいたことがあるので、`std::vector<char>`を使おうか悩んだ。
結局、`reachable[i]`が`bool`を返してくれることが、私のようなC++に不慣れな人にとってはとても扱いやすく感じたので、`std::vector<bool>`をそのまま使用した。Step 2 で少し調べてみる。

# Step 2

## `std::vector<bool>`

[Chromium Code Search - vector<bool>](https://source.chromium.org/search?q=vector%3Cbool%3E&ss=chromium%2Fchromium%2Fsrc)

test でしか `vector<bool>` が使われていなさそう。`vector<char>` がフラグなどの真偽値を持つ用例がないかざっと探したが、見つからなかった。
`flags` で調べてみたら、`uint32_t` (!= `std::vector<uint32_t>`) が使われていた。フラグが32個に収まるなら確かに、普通に二進数で保存すれば良いのか。

ざっと流し見

- [Stack Overflow - Why isn't vector<bool> a STL container?](https://stackoverflow.com/questions/17794569/why-isnt-vectorbool-a-stl-container)
- [Standard C++ - On vector<bool> -- Howard Hinnant](https://isocpp.org/blog/2012/11/on-vectorbool)
- [Stack Overflow - Alternative to vector<bool>](https://stackoverflow.com/questions/670308/alternative-to-vectorbool)
    - `std::deque<bool>`, `std::vector<unsigned char>`, `std::vector<char>`, `std::vector<uint8_t>`, `std::vector<int>` などが代替案として挙げられている。
        - 特に大きな差は見受けられなかったので、`std::vector<uint8_t>` でいいと思う。ただ、具体的な文献は軽く調べた限り見つからなかったのだが、`uint8_t` はごく稀に環境によって定義されていない場合があるよう。

## Trie

他の方々のPRをちょっと眺めて、そういえば Trie というデータ構造があったことを思い出した。Grind 75 に含まれていた LeetCode 208\. Implement Trie (Prefix Tree) でやったやつだ。

(数回の言語化が難しい混乱を挟みつつ)

Step 1 と同じ方法だが、全ての word を試す代わりに Trie を使う方法はどうかと考えた。(-> `step2_trie.py`)

n = |s|, m = |wordDict|, L_avg = average length of words in wordDict, L_max = max length of words in wordDict

とすると、

Step 1 の bottom up DP の解法の時間計算量は、各インデックスに対して wordDict 内の全ての word を試すので O(nmL_avg)

これに対して、wordDict を全て試す代わりに Trie を用いれば、時間計算量は Trie の構築 + 各インデックスからのチェックで `O(mL_avg + n * min(n, L_max))`
Step 2 の第一項 `mL_avg` は `nmL_avg` よりも小さいので、第二項に注目すると `min(n, L_max) << mL_avg` ならば、Trie の方が処理が少なくなる。直感的に考えれば、各入力文字列のインデックスにおいて、wordDict内の全ての文字列、さらに各文字が一致しているかチェックしなければならないところを、最悪でもwordDict内の一番長い文字列の長さしか処理しなくてもよくなるところが、 Trie を扱う利点だろう。

今回の制約から、 Trie の構築が最大 1000 * 20 = 2 * 10^4 回の処理 + DPがだいたい 300 * 20 = 6 * 10^3 で大雑把に合計で 3 * 10^4 回の処理が必要。C++が1秒間に10^8 (~ 10^9) 回の処理を行えるとすると、3 * 10^4 / 10^8 s = 300 us で Step 1 のだいたい 60 ms という見込みよりもかなり速くなりそう。
