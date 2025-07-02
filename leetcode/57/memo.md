# Step 1

## 走査 + 新しいリスト作成

少し、入力リストを改変する方法を考え、やや面倒だなと悩んだが、問題文に新しいリストを作っていいとの言及があることに気づき、そこからはすぐにテストケースをパスする回答を書けた。

手作業だったらどうやるか考え、シンプルに最初からintervalを見ていって、新しく挿入するintervalを区間がかぶる場合は合体させ、そうでないならそのまま新しいリストに入れていけばいいな、と考えた。

時間計算量: O(n), 空間計算量: O(n)

## 再帰 - 1

intervalを一つずつ走査するループは再帰でも表せるなと思ったのでざっと書いてみる (ループは再帰でも書けるのは当たり前か) -> `step1_recursive_1.py`

時間計算量: O(n^2), 各再帰O(n)において新しいリストを作成 (intervals[1:], 返り値のためのリスト結合)O(n)している。
空間計算量: O(n^2), call stackの長さがnで、各フレームでintervals[1:]のスライスも保持している (n-1 + n-2 + ... + 1 = O(n^2))。

とりあえず書いてから、少し考えて、インデックスのみを渡せば新しいリストの作成をせずに済むな、と思った。

## 再帰 - 2

インデックスをhelper関数に渡すことで、スライシングによる新たなリスト作成の手間が省けた。が、コードがかなり複雑になり副作用も持つようになった。この方法を選ぶ理由はあまりないかな。

時間計算量: O(n), 多くても入力リストの長さ (n) + newInterval挿入 (1) 回の再帰。
空間計算量: O(n), call stack, 答え保存用のリスト

# Step 2

## 他の方々の解法

Discordで検索をかけてみたが、この問題を解いた方はいらっしゃらないようだ。

先駆者がいないのでLeetCodeのSolutionsを眺めてみた。なるほど、1. 挿入区間より前、2. 挿入区間と被る、3. 挿入区間より後、という判定において、2番目が終わるインデックスがわかっていればあとは更新した挿入区間と、元のインターバルの残りを付け加えれば良いのか。LeetCode上で多く閲覧されている回答は大体この方法。

私のstep 1の解法だと、挿入区間が被らなくなった時に挿入区間を新しいリストに加えるためのフラグ（かもしくはインデックスを保存するための変数）が必要になってしまうが、どうせ挿入区間を抜けたことを示す変数が必要になるならば、走査のための`i`をそのまま使った方が確かにわかりやすいなと思った。

```python
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        new_intervals: list[list[int]] = []

        i = 0
        while i < n and intervals[i][1] < newInterval[0]:
            new_intervals.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        new_intervals.append(newInterval)
        new_intervals.extend(intervals[i:])
        return new_intervals
```

## 迷ったところ

### 変数名

新しいリストの変数名に迷った。`answer`は曖昧でもう少し情報が欲しいし、step 1では`intervals_after_insertion`としてしまったが、本当に挿入後のインターバルのリストになるのは最後の最後なので、途中経過においてその名付けは語弊を生む。`new_intervals`はどうだろう。

### 副作用

私の再帰の解法もそうだが、渡された`newInterval`を関数内で更新してしまうことに抵抗感がある。思いがけない落とし穴を避けるためにも、個人的にはできるだけ関数は純粋に保ちたい。

### `intervals[i][0]`, `intervals[i][1]`

位置が意味を持つことがコメントなどで明確に共有されていれば良いのだが、`intervals[i][0]`がi番目の区間の始まりを表していていて、`intervals[i][1]`がi番目の区間の終わりを表していることが少しわかりづらく感じる。(位置に意味を持たせるなら、immutableな`tuple`の方が使われている印象。)

```python
interval_start, interval_end = intervals[i]
```

として変数を置きたいが `while`文と組み合わせることを考えるとなかなか上手い形が思いつかない。しょうがないので、`intervals[i][0]`, `intervals[i][1]`は処理やその他文脈から汲み取ってもらうことにする。
