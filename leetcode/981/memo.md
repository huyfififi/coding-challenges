# Step 1

最初は単純に、リストを走査する方法で実装したらTLEになった。

> At most `2 * 10^5` calls will be made to `set` and `get`.

リストを試すときは、setが `2 * 10^5 - 1`回、getが`1`回のときを考えて、オーダー的に大丈夫だろうと思ったのだが、TLEを喰らってからよくよく考えてみたら、

setが `10^5`回、getが`10^5`回の場合、各getで10^5の長さのリストを走査しそれを10^5回繰り返すので、単純 10^10 回の処理が必要で、大体Pythonが10^6回/s処理できるとおくと、10^4s \~= 2.8時間くらいかかる計算になってしまう。

幸い、

> All the timestamps timestamp of `set` are strictly increasing.

という制約があるので、Binary Searchをするのだろう。

`bisect.bisect_left`を用いようとしたが、インデックスの扱いがうまくいかず時間をかなり費やした。
`bisect.bisect_right`を試してからはすぐに回答に辿り着いた。(-> `step1.py`)

[GitHub - cpython/Lib/bisect.py](https://github.com/python/cpython/blob/f8262b84f5b76e45cfea9d73b09657919926850f/Lib/bisect.py#L21)

# Step 2

LeetCodeに投稿されているコードをみても、Binary Searchをどう書くかだけで、大きく私のstep 1からは変わらないl。Binary Search中に返す値 (例えば`result`という変数とか) を更新していく

[cppreference - std::upper\_bound](https://en.cppreference.com/w/cpp/algorithm/upper_bound.html)

C++ではこの関数を使えば良いらしい。

[Google C++ Style Guide - Line Length](https://google.github.io/styleguide/cppguide.html#Line_Length)

> Each line of text in your code should be at most 80 characters long.
> We recognize that this rule is controversial, but so much existing code already adheres to it, and we feel that consistency is important.

80文字なのか。結構短いな。

CPythonの `bisect_left()` と `bisect_right()` を見比べて、脳にいい感じに収まるのを待っている。

```py
def bisect_left(a, x, lo=0, hi=None, *, key=None):
  while lo < hi:
    mid = (lo + hi) // 2
      if key(a[mid]) < x:
        lo = mid + 1
      else:
        hi = mid
  return lo
```

i < lo には key(a[i]) < x のみ
i >= hi には key(a[i]) >= x のみ

```py
def bisect_right(a, x, lo=0, hi=None, *, key=None):
  while lo < hi:
    mid = (lo + hi) // 2
    if x < key(a[mid]):
      hi = mid
    else:
      lo = mid + 1
  return lo
```

i < lo には key(a[i]) <= x のみ
i >= hi には key(a[i]) > x のみ

`=`をどちらに寄せるかだけが違う。

本当にしっくりくるには、もう少し脳内で寝かせないといけなそう。

# Step 3

invariantsをコメントに残すことで、書いていて混乱することを防いだ。

# Step 4

PRを作ってからDiscord内のPRに気づいた。

[この問題を見たとき、同じ key に対する `value` は、 `timestamp` でソートした二分探索木に入れるのがよいと思いました。](https://github.com/sakzk/leetcode/pull/8/changes#r1639814857)

確かにそういう方法もあったか。
