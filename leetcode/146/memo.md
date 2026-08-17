# Step 1

## 思考ログ

`get` と `put` を O(1) で実装しなければならないと聞くと、hash table を使うことが連想されるが、直近で使用されなかった key-value をどう evict するのかは今のところ思いつかない。

例えばカウンタを持って priority queue (heap) を使用するのはどうかと考えたが、`get` と `put` は O(1) にならなそう。

hash table と priority queue を別々に検討して思いつかないので、複数のデータ構造を組み合わせることを考えてみる。

なんとなく dict -> key/value store, heap -> track least recently used key を考えていたのだが...

get -> dict[key]

put -> dict[key] = value, push key and count to the heap, pop until `len(heap) <= capacity`

たまにしか heap の操作をしないなら average で O(1) になりそうな気もするが、heap 操作が連続すれば O(1) では収まらないように思う。

20 分くらい考えたので LLM にヒントを出してもらってみる。

```
かなり subtle にすると、こんなヒントです。
「LRU を特定するために、本当に “使用回数” や “時刻” を数値として保存する必要があるか？」
必要なのは「どれが一番古いか」という順序だけです。
さらに一歩だけ進めるなら、
> get された要素を「最近使われた側」に移動できて、
> 「最も使われていない側」の要素を O(1) で取り除けるデータ構造は何だろう？
今考えている hash table + もう1つのデータ構造 という方向性はかなり良いです。
```

queue, deque を検討して delete by index が O(1) ではないことを考慮した結果、自前で双方向リストを実装して、追加で key -> node の hash table を持てば良さそうだと思った。
双方向リストで、取り除くべき場所がわかっているならば、reference の操作で繋ぎ換えが行える。そういえばそんなようなことを大学四年生の時のUNIXプログラミングの講義でやった記憶がある、当時はほとんど理解できていなかったが。
実装がかなり面倒そうだが、方針としては合っていそうだ。

get -> 双方向リストから当該箇所を削除し、先頭につける。値を返す。

put -> 
値が key-value store に存在: 双方向リストから当該ノードを外し、先頭につける。値を key-value store に保存。
値が key-value store にない: 双方向リストの先頭に新しい値をつける。capacity を超える分、双方向リストの最後尾を削除。値を key-value store に保存。

あとはやるだけだが、少し骨が折れそうだ。

一瞬、双方向である必要がなくないか？とも思った (237. Delete Node in a Linked List) が、リファレンスの付け替えや保持するデータをパッと思い浮かべると双方向が良さそうだ。

`step1.py`

if condition がかなり複雑になってしまったが、LeetCode 上の実行時間の分布を見るに、これが一番速いやり方のようだ。

制約が

> At most `2 * 10^5` calls will be made to get and put

なので O(nlogn) くらいまでLeetCode上で許容されそう。LeetCode 上の実行時間の分布を見ると、私の複雑で、特に最適化もしていない doubly linked list を使用する方法よりも遅いところに分布の山があるので、get/put に O(log n) かかる方法も多く含まれているのかもしれない。複雑な `step`.py` をリファクタリングすることと共に ~Step 2 で取り組む。~ -> よく考えてみたら、私が Step 1 で Priority Queue を使う方法を捨てたのは、

> The functions get and put must each run in O(1) average time complexity.

というのが問題文にあったからだった。LeetCode 上ではテストケースをパスするかもしれないが、Priority Queue を使用する方法は問題文を読む限り想定解ではないのだろう。

# Step 2

## ChatGPT と色々相談してみる

- head だけ dummy を用いていたが、tail でも dummy を使えば、追加・削除する node がいつでも `next` と `prev` を持つようになって、条件分岐がを減らせる。
- `\_\_detach\_cache` と `\_\_attach\_cache` から `key\_to\_node` の扱いを外して関数内でやることをシンプルに、結果的に余分な Hash Table の操作を削減。

## 他の方々のPRを見てみる

- [tom4649 さんのPR](https://github.com/tom4649/Coding/pull/72)
	- OrderedDict を使えばもっと簡単に書けるのか、[move_to_end](https://docs.python.org/3/library/collections.html#collections.OrderedDict.move_to_end) と [popitem(last=False)](https://docs.python.org/3/library/collections.html#collections.OrderedDict.popitem) があるの便利だな。dict でも insertion order は保持されるので、OrderedDict は頭の中のすぐ使える部分にはないな。
- [t0hsumi さんのPR](https://github.com/t0hsumi/leetcode/pull/16)
	- CPython の `lru\_cache` 実装への言及がある。
		- [https://github.com/python/cpython/blob/e3287f631f3c88ed80191aa222e7fc4ba91edd17/Lib/functools.py#L609](https://github.com/python/cpython/blob/e3287f631f3c88ed80191aa222e7fc4ba91edd17/Lib/functools.py#L609)
			- ListNode を `[PREV, NEXT, KEY, RESULT]` で表しているの面白いな。
			- circular doubly linked list with a single sentinel root だ。これはOdaさんもレビューコメントで残されている。

TODO: Implement OrderedDict approach
