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
