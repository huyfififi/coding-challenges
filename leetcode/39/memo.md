# Step 1

candidatesの最大要素数が30で、ありえないが多めに見積もるために全てのcandidateが2、targetが40だとすると、30^20通りくらいのオーダーの計算が必要になりそう...？
かなり苦しいが、とりあえず思いついた強引な方法を実装してみると一応テストケースをパスした。-> `step1.py`

Coin Change となんだか似ているよなぁ... 問題は重複をどう弾くかだが...
Coin Change に取り組んだ時はcoinsをソートしてもそこまで旨味を感じなかったが、今回の場合candidatesをソートして、non-decreasing order に並ぶcombinationだけを考えるようにすれば重複をはじく手間が省けそうだ。
いやいや、よく考えたらソートする必要はない。単にダブらないようにするのに、試してもいいcandidatesのindexを単調増加させていけば良い。
再帰だったら

```
l.append()
recursive_call(l)
l.pop()
```

として余分なコピーを減らす方法に慣れているので、一旦再帰で -> `step1_improved_recursive.py`
