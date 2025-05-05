# Step 1

## `step1_recursive.py`

再帰関数を用いる解法は特に引っかかることもなく書けた。左右片方でも既にアンバランスならearly returnできるが、heightを返すと約束した以上、ダミーの値を返すのはやや抵抗感があった。

ノードの数をn、木の高さをhとして

時間計算量: O(n), 全てのノード（とNoneの子ノード）を一度訪れるため。
空間計算量: O(h), 再帰関数呼び出しのスタックの最大量は h + 1

## `step1_iterative.py`

何日か脳内で寝かせてできたのがiterativeな解法。再帰をstackで表現することはわかったが、左右の結果が必要とのことでpost-order traversalをstackで表現することがしっくりくるまで数日要した。

時間計算量: O(n), 各ノード（とNoneの子ノード）に対して定数時間の操作を行うため。（が、early returnはできる）
空間計算量: O(n), 全てのノードにおいての部分木の高さをhash tableに収めているため。

# Step 2

- [colorboxさんのPR](https://github.com/colorbox/leetcode/pull/12)
    - 一つのhelper関数に全てを任せるのではなく、高さを見る関数は別で切り出す方法。
- [Mike0121さんのPR](https://github.com/Mike0121/LeetCode/pull/4)
    - helper関数内で外側の関数と同じ変数名を用いると混乱するだろう、また途中経過だから`root`という変数は避けた方がいいだろう、との指摘と理解。
- [NobukiFukuiさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/19)
    - helper関数の名付けは私もまだ接してきたサンプル数が足りなくて善し悪しが判断しかねる。
- [Kitaken0107さんのPR](https://github.com/Kitaken0107/GrindEasy/pull/16)
    - [hayashi-ayさんのコメント](https://github.com/Kitaken0107/GrindEasy/pull/16#pullrequestreview-1984849457) "再帰の処理をよくよく追っていくとheightとisBalancedでノードを同じように辿っているので一緒にしてしまうという選択肢もあると思います。" が、うまく効率化の方針を言い表されていて納得感があった。

helper関数の命名だけ、少し考える必要があるかも。他は先駆者の方々と大体解き方が同じ。

## 迷ったところ

コメントを残さないと何番目の値が何を表すかわかりにくいなら、最初からクラスを作ってしまう？と思って

```
class BalanceStatus(NamedTuple):
    height: int
    is_balanced: bool
```

を置いてみたが、あんまりいい抽象ができたようには思えなかった。結局`tuple`を見たら順番に意味があるのだとPythonに慣れている人なら理解するし、難しいことはせず必要ならコメントを残せばわかりやすいと思う。
	- 昔、プロジェクトの先輩に、コメントは更新忘れとかがあるから過信せず、コメントを残すくらいならとにかく実際の実装をわかりやすくするべき、という指摘を受けた記憶が蘇ってくる。

一応、関数名がisBalancedだったので、helper関数内の変数を`is_balanced`とするのは将来的に関数名をsnake\_caseにした時に事故が起こりやすいような気がして、`_is_balanced`にしておいた。

# Step 3

## ミスしたところ

- helper関数呼び忘れ (iterative)
- `node_to_height`の更新忘れ (recursive)
- あまり考えずに書いたらbase case (None node)の時になぜか`is_balanced=False`を返してしまった (recursive)
- type annotation 内の`TreeNode`を`Treenode`にtypo (recursive)
- stackに3回同じnodeを入れてしまった (iterative)
- helper関数呼び出し時に`is_balanced_helper(root)[1]`を`is_blanced_helper(root)[1]`とtypo (recursive)
- `left_height`を入れるべきところに`left_is_balanced`を入れてしまった。(recursive)
- stackにvisitedフラグを入れ忘れた (iterative)
- `node_to_height[node.left]`を`node_to_height(node.left)`としてしまった (iterative)

気持ちゆっくりめにタイピングし、行の意味をある程度見直すようにしても、なかなかtypoが避けられなく、厳しい。

# Feedback

- 典型コメント集にも載せてある[Odaさんのコメント](https://discord.com/channels/1084280443945353267/1201211204547383386/1247145320098566144)

> いや、私の良くするたとえ話としてね、木の全ノードに部下を立たせるんですよ。
> そうすると、nonlocal って、部下たちのいる部屋に共通の看板を立てておいて、全部下がその看板に書いたり消したりするんですよね。
> それだったら、部下同士のやり取り(関数呼び出し)の中で、自分より下の部分の `max_sum` の情報も報告するようにしたほうがスマートじゃないでしょうか、ということです。
> たとえば、こっちの方がスレッド増やしたくなったときに並列性が良さそうです。

が新鮮な視点だった。再帰関数をかくと時たまnonlocalを使用してしまうが、確かに避けた方が良さそう。

- [Odaさんのコメント](https://discord.com/channels/1084280443945353267/1230079550923341835/1234534017181814795)

> 「k 番目の数字を報告しろ。k 人いない場合には、代わりに人数を報告しろ。」

二つの命令を出す（返り値に二つの意味を持たせる）と、一度の連絡網で結果が返ってくると、想像がつきやすい。わかりやすい例でありがたい。

- この問題をループに直すことは難しい、という私の観察は合っていたよう。dictを使用せずとも、PythonのListを渡して処理してもらうことも可能そうだが、今の私には難しすぎるので一旦スキップしておく。
