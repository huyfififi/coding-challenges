# Step 1

合計値が `sum(nums) // 2` と一致する組み合わせを見つければいい、と考えた。
素直にやるなら、各 index においてその要素を使うか使わないかで分岐していって、subsetの合計値をチェックしていけばいいのだが...

> `1 <= nums.length <= 200`

という制約から、各インデックスで2つに分岐すると考えると 2^200 通り試すことになってしまう。これはかなり多めに見積もった値であり、枝刈りができるとはいえ、TLEするだろうなと予想はつく。一応実装してみたが、案の定TLEした。-> `step1_tle.py`

何も思いつかないので、問題のTopicsを覗いてみたらDPを使うっぽい。
TLEした方法だと、再帰関数が二つの引数 `(subset_sum, checking_index)` を必要としていて、これをメモ化したところで... と思ったのだが、後々に同じものが出てくる可能性があるか。

試しに `@functools.cache` をヘルパー関数につけてみたら、39番目のテストケースでTLE していたものが 100 番目のテストケースでMLE するようになった。高速化はできたが、記録しておかなければならないペアがとても多くなってしまうので、筋の良い方法ではなさそう。

少しどうにか動的計画法を使えないか考えてみたが、思いつかなかったので、LeetCodeのDiscussionを眺めて、実装した。-> `step1.py`
逆順で辿ることで、同じ要素を２回使用してしまうことを防いでいるみたいだ。なるほど。

まぁ、一旦こういう手法もあるんだくらいに留めて練習してみようかな。

# Step 2

[Wikipedia - Subset Sum Problem](https://en.wikipedia.org/wiki/Subset_sum_problem)

> The subset sum problem (SSP) is a decision problem in computer science. In its most general formulation, there is a multiset *S* of integers and a target-sum *T*, and the question is to decide whether any subset of the integers sum to precisely *T*.

> SSP is a special case of the knapsack problem and of the multiple subset sum problem.

この問題は、各itemが最大でも一回しか使えない 0/1 Knapsack Problem に分類されるらしい。

# Step 4

[https://github.com/hemispherium/LeetCode\_Arai60/pull/10#discussion\_r2618523247](https://github.com/hemispherium/LeetCode_Arai60/pull/10#discussion_r2618523247)

いつでも参照渡しが効率的なわけではない :eyes:
