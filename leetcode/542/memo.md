# Step 1

2つの方法が思いついた。

## Two-pass

まずは左上から右下に0 (からの距離) を波及させて、その後右下から左上に0 (からの距離) を波及させる方法。
数年前に友人と勉強会をした時、似たような問題 (かどうかは定かではないが) を友人がこの方法で解いているのを隣で見て、確かにうまく行きそうだな、こんな方法あるのかと思った記憶がある。

時間計算量: O(mn)
空間計算量: O(1) (とりあえず入力を変更してしまう形で実装した。)

## Loop + DFS

シンプルに、各0から最短距離を波及させていく方法もあるな、と思ったが、この方法の時間計算量はO(mn)より大きくなりそうなのでTLEだろう。

一応書いて走らせてみたが、案の定TLEだった。-> `step1_brute_force_recursion_tle.py`

時間計算量: O((mn) ^ 2)? 0が取り得る個数は`mn`、本当は早めにreturnしているが、それがなかったとするとmatrix内の全てに最短距離を波及させていくので`mn`、よって`mn * mn`だが、実際のところどうなのだろう...。

手元の環境で試してみた。

TODO: 実験環境について詳しく

| mn    | (mn)^2    | s (time taken)  | s / ((mn)^2)      |
| ----- | --------- | --------------- | ----------------- |
| 4     | 16        | 0.0004391670227 | 0.00002744793892  |
| 16    | 256       | 0.001873016357  | 0.000007316470146 |
| 200   | 40000     | 0.1182088852    | 0.00000295522213  |
| 1000  | 1000000   | 3.642772913     | 0.000003642772913 |
| 3000  | 9000000   | 35.14230704     | 0.000003904700783 |
| 5000  | 25000000  | 98.57335901     | 0.000003942934361 |
| 8000  | 64000000  | 254.4024489     | 0.000003975038264 |
| 10000 | 100000000 | 398.5889831     | 0.000003985889831 |

s / ((mn)^2) の値がほぼ一定のように見えるので、このプログラムの実行時間は (係数) * ((mn)^2) で決まりそう, i.e., 時間計算量はO((mn)^2)のように考えられる。

空間計算量: O(mn) 新しく作るmatrixの大きさが`mn`、左上の0から再帰関数を呼んで右下まで行くと`m + n`で、これがcall stackの最大長。O(mn) + O(m + n) = O(mn)

## BFS

ChatGPTに最低限のヒントをお願いしたところ、call stackではなくqueueを使いなさい、と言われたので、なるほど、各0において最短距離の更新を終わらせてから次の0を処理するのではなく、全ての0から少しずつ処理した範囲を広げていけば、同じセルを何度も更新せずに済むのか、と気づいた。

空間計算量: O(mn)

# Step 2

一社Discord内に先駆者が見つからなかったので、LeetCodeのSolutionsを眺めてみる。

私はqueueに「最短距離未更新のセル」を入れていたが、ぱっと眺めてみると、queueに最短距離更新済みのセル」を入れている解法が多かった。確かにこれなら処理が各0から伸ばして重なった範囲で止まる。

また、目を通した限り全ての解法で、queueに追加されるセルの数を抑えるために、queueに入れる前に範囲をチェックする方法が採られていた。実行時間・メモリ使用量を少しでも抑えるためなのか、今回の問題ではそちらの方が読みやすくなるからあえてなのかはわかりかねる。

queueに何を入れるのか約束できている限り、範囲チェックを後でやる方法でも、LeetCodeのSolutions（や、一社内のPR）でよくみられるでもどちらでも良さそうだ。

```python
from collections import deque


class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        num_rows = len(mat)
        num_cols = len(mat[0])

        queue: deque[tuple[int, int]] = deque()
        for row in range(num_rows):
            for col in range(num_cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = float("inf")

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            row, col = queue.popleft()
            for row_diff, col_diff in directions:
                row_update = row + row_diff
                col_update = col + col_diff
                if (
                    0 <= row_update < num_rows
                    and 0 <= col_update < num_cols
                    and mat[row_update][col_update] > mat[row][col] + 1
                ):
                    queue.append((row_update, col_update))
                    mat[row_update][col_update] = mat[row][col] + 1

        return mat
```
