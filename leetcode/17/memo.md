# Step 1

各桁の間に関係性がなさそうなので、素直に全通り生成していく問題かなと思った。

> `1 <= digits.length <= 4`

で、1 つの digit が最大 4 つの文字を取りうるので、`4 ^ 4 = 2 ^ 8 = 2 ^ 10 / 2 ^ 2 = 1024 / 4 = 256` 通りの結果を最悪作ることになる。
木を考えると、一段目が 4、次が16、64、256 と続いて、全部で 340 のノードが存在し得るが、これは C++ が 1秒間で 10^8 - 10^9 回の処理を行えることを考えると、実行時間は問題にならないように思う。
最終的に長さ 4 のstring を 256 個持つことになるが、char が 1 byte、4 つで 4 bytes、std::stringのサイズに詳しくない (Step 2 で調べる) ので一旦そこは無視しても、256 * 4 bytes = 1 KB。特に問題になるような大きさではないだろう。

時間計算量: O(n * 4 ^ n) (string construction + generate all possible combinations)
空間計算量: O(n * 4 ^ n) (the result holds 4 ^ n strings with length of n)

テストケースは無事にパスしたのだが、LeetCode 上の実行時間・補助空間使用量の順位が最下位に近い。constant くらいしか違わなそうだが、私の解法よりも効率の良い解法がありそうだ。~Step 2 で見てみることにする。~ と思ったのだが、これ backtracking で行けるのでは？ C++のsyntaxを思い出すことにいっぱいいっぱいになってしまっていたが、Pythonだったらnested functions を書くのが楽なので helper 関数を用意して backtracking という方法がすぐに思いついたのにな、悔しい。
