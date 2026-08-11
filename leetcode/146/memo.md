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
