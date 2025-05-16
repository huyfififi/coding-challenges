# Step 2

変数名がなかなか悩みどころ。

`prev`, `curr`, `next`だと、reverseしたlistにおける"前"や"次"なのか、元のlistにおける"前"や"次"なのか少し混乱する。

また、処理をどうグループ化するかも悩ましい。while文の中に4つの短い処理をスペース無しで並べると、それらに順序的な関係がないような印象を覚えてしまうので (偏った感覚？)、スペースを入れたいのだが

```python
while node:
    # 次に処理するnodeを待避
    next_node_to_reverse = node.next

    # 繋ぎかえて reversed listを伸ばす    
    node.next = reversed_head
    reversed_head = node

    # 処理するnodeを進める
    node = next_node_to_reverse
```

と見るか

```python
while node:
    # 次に処理するnodeを待避
    next_node_to_reverse = node.next

    # 処理中のnodeのreferenceをひっくり返す
    node.next = reversed_head

    # referenceの更新
    reversed_head = node
    node = next_node_to_reverse
```

と見るかで少し悩んだ。

## 他の方々のPRを見る

[h1rosakaさんのPR](https://github.com/h1rosaka/arai60/pull/10)
	- helper関数に二つNodeを渡してしまうやり方は考えつかなかったな。この問題に関しては、様々な書き方がありそう。
[potrueさんのPR](https://github.com/potrue/leetcode/pull/7)
	- 残されたコメントを見る限り、再帰的な解法では、せっかく問題を分解しているのだから、reverseしたlistの先頭と末尾を返して1つのステップ、直接隣り合ったNodeだけ操作する方法の方が自然...なのだろうか。
[5ky7さんのPR](https://github.com/potrue/leetcode/pull/7)
[irohafternoonさんのPR](https://github.com/irohafternoon/LeetCode/pull/9)
[garunituleさんのPR](https://github.com/garunitule/coding_practice/pull/7)

## 再帰的な解法

どの解法も納得感があるが、最近再帰関数でペアを返すことで解ける問題の幅が広いことに気づき、もう少し練習したいという思い、一つのステップでやる操作が直感的、(また、現時点で言語化できない個人的な好みにより)、step 3はstep1のペアを返す方法で実装することにする。

### 別解1

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head

        reversed_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None  # for reversed tail
        return reversed_head
```

### 別解2

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse_list_helper(
            prev_node: Optional[ListNode], curr_node: Optional[ListNode]
        ) -> Optional[ListNode]:
            if curr_node is None:
                return prev_node

            reversed_head = reverse_list_helper(curr_node, curr_node.next)
            curr_node.next = prev_node
            return reversed_head

        return reverse_list_helper(None, head)
```
