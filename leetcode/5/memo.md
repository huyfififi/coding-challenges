# Step 1

## `step1_brute_force.cpp`

動的計画法などが頭をよぎったが、上手い方法が思いつかない。
C++ なら 1 秒間で `10^8` (`~10^9`) 回くらいの処理が行えるので、

> `1 <= s.length <= 1000`

という制約から、部分文字列を決める start と end を全通り試して (かなり大雑把に) `10^6`, 回文チェックで大体 `10^3`, 合わせて `10^9` 回くらいの処理が必要になりそうだが... 枝狩りをすれば 1 秒くらいで終わるか？ -> `step1_brute_force.cpp` で全てのテストケースをパスできた。

時間計算量: `O(n^3)` (`部分文字列のstart/endの組 * 回文チェック`)、空間計算量: `O(n)` (最悪入力文字列と同じ長さのものを作って出力しなければならない。)

だが、これは効率の良いやり方ではないだろうな。

## `step1_dp.py`

二次元配列で各 (start, end) のペアが palindrome かどうかを保持すれば、回文チェックが O(1) でできそうなのはわかったが、それをどう埋めていけば良いのかわからなかった。
ChatGPTと数回やりとりした後の私の理解は、以下の通り。

`is_possible[i + 1:]` is needed to compute `is_possible[i]`. Therefore, it is natural to think about filling it in backwards
In the same way, `is_possible[:i - 1]` should be computed before `is_possible[:i]`. Therefore, it makes sense to move end from left to right.

## `step1_manacher.py`
