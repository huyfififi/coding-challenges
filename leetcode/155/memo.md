# Step 1

Cracking the Coding Interview で 見た気がするが、関連する記憶がない。

なんだか見覚えのある問題として LeetCode 232\. Implement Queue using Stacks が思い起こされるが、今回の問題は

> You must implement a solution with O(1) time complexity for each function.

とあり、amortizedではないんだよな。とすると、シンプルに O(1) で全てのメソッドを実装できる方法があるのだろう。

複数のデータ構造を持つのかなと予想するが... min を浮かせて保持するとどうなるだろう？

queue or stack <-> min <-> queue or stack

いろんな組み合わせを脳内で試したが、何も思いつかなかった。

minへのアクセスが O(1) なのを考えると、min-heap?とも思ったが、挿入・削除が O(1) で済まない。

非常に悔しいが、hint を見ると

> Consider each node in the stack having a minimum value. (Credits to @aakarshmadhavan)

なるほど！！
