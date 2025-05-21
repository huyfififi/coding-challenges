# Step 1

Linked List系の問題は、referenceの操作が正しくできるかどうかが測られているので、(dummy以外)新しいNodeを作らない解法が求められているのだろう、と予想する。

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

    # 次に進むためのreferenceの更新
    reversed_head = node
    node = next_node_to_reverse
```

と見るかで少し悩んだ。

## 他の方々のPRを見る

[h1rosakaさんのPR](https://github.com/h1rosaka/arai60/pull/10)
	- helper関数に二つNodeを渡してしまうやり方は考えつかなかったな。この問題に関しては、様々な書き方がありそう。
[potrueさんのPR](https://github.com/potrue/leetcode/pull/7)
	- 残されたコメントを見る限り、再帰的な解法では、せっかく問題を分解しているのだから、reverseしたlistの先頭と末尾を返して1つのステップを簡潔にする方法が自然...なのだろうか。
[5ky7さんのPR](https://github.com/5ky7/arai60/pull/8)
[irohafternoonさんのPR](https://github.com/irohafternoon/LeetCode/pull/9)
[garunituleさんのPR](https://github.com/garunitule/coding_practice/pull/7)

## 再帰的な解法

どの解法も納得感があるが、現時点で言語化できない個人的な好みにより、step3はstep1と同様にペアを返す方法で実装することにする。
- 最近、再帰関数でペアを返すことで解ける問題の幅が広いことに気づいた。
    - "If the only tool you have is a hammer, it is tempting to treat everything as if it were a nail."

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

# Step 3

Step 3までやってようやくしっくりきたのだが、私のiterativeな解法は元のリストを先頭→末尾に進みながら繋ぎかえが発生するが、recursiveだと元のリストの末尾→先頭の順で繋ぎかえが発生している(Stackを用いているため逆順になるのは当たり前だが)。

# Step 4

## Tail Recursion

末尾再帰 (tail recursion)とは、再帰のパターンの一種で、再帰関数において再起呼び出しが処理の末尾にあり、その戻り値をそのまま関数全体の戻り値として使用しているパターンを指す。
末尾再帰の利点は、通常の再帰と異なり、再起呼び出しの後に追加の計算がないため、呼び出し側のスタックフレームを保持する必要がなくなる点にある。
そうすると、ループ構造に機械的に書き換えられる、または末尾呼び出し最適化(tail call optimization)によってスタックフレームを積まずに済む。

```python
def reverse_the_first_and_append_the_second(reversing, appending):
    if reversing is None:
        return appending
    reversing_tails = reversing.next
    reversing.next = appending
    return reverse_the_first_and_append_the_second(reversing_tails, reversing)
```

```python
 def reverse_the_first_and_append_the_second(reversing, appending):
    while reversing is not None:
        reversing_tails = reversing.next
        reversing.next = appending
        reversing, appending = reversing_tails, reversing
    return appending
```

### Resources

[Tail recursion - HaskellWiki](https://wiki.haskell.org/index.php?title=Tail_recursion)

> A recursive function is tail recursive if the final result of the recursive call is the final result of the function itself. If the result of the recursive call must be further processed (say, by adding 1 to it, or consing another element onto the beginning of it), it is not tail recursive.
> In many programming languages, calling a function uses stack space, so a function that is tail recursive can build up a large stack of calls to itself, which wastes memory. Since in a tail call, the containing function is about to return, its environment can actually be discarded and the recursive call can be entered without creating a new stack frame. This trick is called tail call elimination or tail call optimisation and allows tail-recursive functions to recur indefinitely.

[3.1.1.5. Tail Recursion · Functional Programming in OCaml](https://courses.cs.cornell.edu/cs3110/2021sp/textbook/data/tail_recursion.html?q=)

[github.com/ocaml - ocaml/stdlib/list.ml](https://github.com/ocaml/ocaml/blob/d325f299896417c5f1d477171135acfdf402e770/stdlib/list.ml#L57)

```ocaml
let rec rev_append l1 l2 =
  match l1 with
    [] -> l2
  | a :: l -> rev_append l (a :: l2)

let rev l = rev_append l []
```

これはOdaさんにいただいた末尾再帰のReverse Linked Listのコードとほぼ一致する。

```python
def reverse_the_first_and_append_the_second(reversing, appending):
    if reversing is None:
        return appending
    reversing_tails = reversing.next
    reversing.next = appending
    return reverse_the_first_and_append_the_second(reversing_tails, reversing)
```

### Examples

階乗を求めるプログラム(末尾再帰ではない形)。この方法では、再起呼び出しの結果にnをかけている。

```python
def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)
```

末尾再帰で書くと

```python
def factorial(n: int, accumulated: int = 1) -> int:
    if n == 0:
        return accumulated
    return factorial(n - 1, accumulated * n)
```

この方法では、関数内で最後にやることが再起呼び出しの結果を返すことになっている。

## Feedback

- **再帰 <-> ループ間変形**
    - 末尾再帰
- 変数の末尾にコメントを書くとフォーマットが大変なので、素直にdocstringに書いた方がいいかも
- 意味ではなく操作の順番からの命名 (previous) に気を付ける、パズルを作らないように
- 四行くらいしかないなら空行を入れても読みやすさは変わらないかも
    - どうせ空行を入れるなら、コメントを積極的に入れてもいいかも
- `reversing`, `appending`という命名
- PEP8の (sparingly) というニュアンスに気づかなかった "Extra blank lines may be used (sparingly) to separate groups of related functions."
- `rest*`, `*_tails`
