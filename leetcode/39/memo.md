# Step 1

candidatesの最大要素数が30で、ありえないが多めに見積もるために全てのcandidateが2、targetが40だとすると、30^20通りくらいのオーダーの計算が必要になりそう...？
うまく実行時間の見積もりができなくてかなり苦しいが、とりあえず思いついた強引な方法を実装してみると一応テストケースをパスした。-> `step1.py`

Coin Change となんだか似ているよなぁ... 問題は重複をどう弾くかだが...
Coin Change に取り組んだ時はcoinsをソートしてもそこまで旨味を感じなかったが、今回の場合candidatesをソートして、non-decreasing order に並ぶcombinationだけを考えるようにすれば重複をはじく手間が省けそうだ。
いやいや、よく考えたらソートする必要はない。単にダブらないようにするのに、試してもいいcandidatesのindexを単調増加させていけば良い。

また、再帰だったら

```
l.append()
recursive_call(l)
l.pop()
```

として余分なコピーが減らせる方法がすぐ実装できるので、一旦再帰で -> `step1_improved.py`

その後、recursiveでできるならiterativeでもできると少し考えてみたのだが、各stackの要素にcombinationの新しいコピーを入れない方法は、かなり煩雑になりそうだったので一旦やめておく。

枝刈りがあるとき、どう計算量を導き出せばいいのかわからない... Climbing StairsはO(1.6^n)くらいになることが思い出されるが...
-> 他の方々のPRとコメントを見る限り、計算量の見積もりは少し難しそう。

# Step 2

PRをざっと眺めると、`step1_improved.py`が皆さんの解法と同じ感じ。

combinationの構成要素数が20 (\* candidate min: 2 = target max: 40 ) よりも少ないので、`total`を保持せずに毎回`sum()`しても定数倍でやや遅くなるがそこまで問題にはならなそう。

Coin Change と同様に、candidatesをソートしておいて早めにループを抜けるのも細かい最適化案としてはあるか。

至る所でbacktrackという用語が使われていたのだが、初耳だった。調べてみる。

[Reddit - I don't understand backtracking at all. (信憑性-低)](https://www.reddit.com/r/leetcode/comments/yv3gth/i_dont_understand_backtracking_at_all/)

> Backtracking is just DFS on tree except there's no pre-defined tree. You have to build your own tree by passing the states through parameters.

信憑性は低そうだが、なんだか腑に落ちた。

Antti Laaksonen - Guide to Competitive Programming

> A *backtracking* algorithm begins with an empty solution and extends the solution step by step. The search recursively goes through all different ways how a solution can be constructed.

-> chessのqueensをおいていく問題

[Wikipedia - Backtracking](https://en.wikipedia.org/wiki/Backtracking)

> **Backtracking** is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction or enumeration problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.

上の本のクイーン問題も、探索が終わったら共有のstate?への変更をrevertしていたな。

こう読むと、私の回答では

```
combination.append(candidates[i)
find_target_combinations()
combination.pop()
```

というパターンがbacktrackingたらしめているのだろう。手元の資料が乏しく、あまりはっきりとしたことはわからないが...
