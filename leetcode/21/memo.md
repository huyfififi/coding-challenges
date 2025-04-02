# Step 1

## 感想

一見簡単に見えたが、行数が増えreferenceの処理が絡むとバグのないコードを書くのがかなり難しく感じ、とりあえずテストケースをパスするコードは書けたものの、恐ろしく読みにくいものになってしまった。再度、気を引き締めたい。

再帰的なアプローチの方が課題を分割した一つのステップに集中できて楽に書けたが、数日後の自分がどちらの解法を好む・再現しやすいと感じるかは現時点ではわからない。

# Step 2

## Step 1の間に考えたこと

- 同じような処理をlist1とlist2を入れ替えただけで2回行っており、typoや書き忘れのバグが起きる確率が（厳密ではない議論として）単純に2倍になっているのではないかと思った。list1とlist2は入れ替えても問題がなく順序や優劣がないので、共通のfunctionを書いて使いまわせないか、と考えた。単純な操作を2回繰り返しているだけなので、わざわざ関数で包んでしまうと逆にわかりづらくなるような懸念もある。
- referenceの操作が多く頭がこんがらがりがちなので、どこか回数を減らせる（？）操作があればシンプルにしたいと思った。

## 他の方々のPRを見て

- [azriel1rfさん](https://github.com/azriel1rf/leetcode-prep/pull/6)
	- `dummy = ListNode()`を作ることでhead周りの処理を省くことができている。
	- PEP8に"Also, beware of writing if x when you really mean if x is not None – e.g. when testing whether a variable or argument that defaults to None was set to some other value."とあり、azriel1rfさんは`is not None`と明記していた。[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)でも"Always use if foo is None: (or is not None) to check for a None value."とあるので、こちらに従おうと思う。
- [kzhraさん](https://github.com/kzhra/Grind41/pull/3)
	- [odaさんのコメント](https://github.com/kzhra/Grind41/pull/3#discussion_r1597538900)"このノードは、再帰構造を変形したために形式的に必要となったもので返り値には関わらないものであるという意図を強く出すと dummy と呼びたくなります。"が私にない思考だったので興味深かった。`dummy`という変数名を使っていきたい。

他の方々のPRもいくつか流し見したが、step 1の間に考えた可換な処理を抜き出すことは逆にコードを複雑にしそうだと思った。

## [niits's solution on LeetCode](https://leetcode.com/problems/merge-two-sorted-lists/solutions/6048156/video-using-dummy-pointer-and-recursion-solution-as-a-bonus)

```
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val > list2.val:
            list1, list2 = list2, list1

        list1.next = self.mergeTwoLists(list1.next, list2)
        return list1
```

必ず`list1.val <= list2.val`になるようにListを入れ替えることで`self.mergeTwolists()`を呼ぶときの条件分岐をなくせている。こういう方法もあるのか。最初の`return list1 if list1 else list2`は似たような文字が並んでいて目が滑るので真似しなくてもいいかなと思った。

## Step 3

- `curr = curr.next`を忘れがち

コード自体はstep 2と大きく変化がなかったので省略。
