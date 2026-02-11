# Step 1

Follow up を見なければ、典型的なソートアルゴリズムを実装すればループが `n^2` 回かかるとしても `1 <= n <= 300` という制約から、Pythonが1秒間で`10^6`回くらいの処理が行えるとすると、100 ms くらいのオーダーで終わると予想される。

記憶が戻ってきた順に、

1. selection sort
2. bubble sort
3. insertion sort (自信なし)

記憶が曖昧なので、誤っているかもしれない。Step 2 で実装が合っているか確認することにする。

5年前にコーディングインタビュー対策した時にこの問題をやったことがあったので、Follow Up の解法も知っていた (-> `step1.py`)。今はもう少し見える景色も広がり、変数名に少し気を遣えたり、インデックスの扱いで間違えても脳内デバッグがある程度できるようになった気がする。

# Step 2

LeetCodeにポストされている解法を眺めていたら、カウンターを用いる方法を発見。確かに、0, 1, 2しか現れないので、その出現回数を数えて、それをnumsに詰めていったらできるな。(`step2_counter.py`)

[Wikipedia - Selection sort](https://en.wikipedia.org/wiki/Selection_sort)

Selection sortのページを眺めている限り、step 1 で実装した理解で合っていそう。今最小にしようとしているポジションの値が、既に自分を含めてまだソートされていない部分の最小であった場合swapをスキップする実装が提示されているが、同じポジション同士でswapしてもロジックとしては変わらないし、swapのスキップの条件分岐がない方が脳内フローチャートが簡潔に収まるような気がする。

[Wikipedia - Bubble sort](https://en.wikipedia.org/wiki/Bubble_sort)
[Northern Illinois University CS501 Bubble Sort](https://faculty.cs.niu.edu/~winans/CS501/Notes/Sorting_Algorithms/bubble_sort.html)

私のStep 1 の解法とほぼ同じだと思うが、ちょっと思っていた書き方と違った。pseudocode を書き起こすとこうなりそう (-> `step2_bubble_sort.py`)。
swapが起こらなかったら、既にソートされていることがわかるので早めにループを打ち切れる。
また、後方に最大の値を集めていくことを利用して、ループ範囲を狭めていく最適化もあるように見受けられる。
Pythonはdo-whileがないので、便宜上 `swapped=True`で初期化しているが、ちょっと読み取りづらいかも。

[Wikipedia - Insertion sort](https://en.wikipedia.org/wiki/Insertion_sort)

こちらの理解も合っていそう。だが、言語化できないちょっとした引っかかりがあり、少し脳内に寝かせる必要がありそう。

# Step 4

Tried 4 colors problem -> `step4_4_colors.py`

TODO:

- Try 5 colors
	- I may be able to simply add one more pointer do extend the swapping logic
- Reply back to サザンカ-san
- Check Noda-san's solution
