### step 1

ぱっと見で思いつくのは
- brute-force (time complexity: O(n^2), space complexity: O(1))
- sorting and two pointers (time complexity: O(nlogn) with Timsort, space complexity(n))

Solutionsを確認したところ、hash tableの利用で time complexity: O(n)で解けることに気づく。

#### 反省事項

- 落ち着いてconstraintsの確認・他の解法の模索をすることを怠ってしまった。

### step 2

実装には困らなかったが、コード内コメントをどこまで残していいのか少し悩んだ。

### step 3

特になし

### step 4

#### Feedback

- Fix the misuse of type annotations.
- Rename the dictionary to a more descriptive name.
- Avoid using the "walrus operator" in this case: two things happen in the single line.
- Return early to reduce the cognitive load on readers.
- The result of tuple sorting is obvious, so making it explicit is unnecessary.
- Don't leave comments about time/space complexity.
- Use a single trailing underscore to avoid naming conflicts with Python keywords (PEP 8).
- Remember that time/space complexity is not the highest priority—programs exist to serve end users.
