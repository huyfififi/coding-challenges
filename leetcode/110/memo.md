# Step 1

再帰関数の方は特に引っかかることもなく書けた。左右片方でも既にアンバランスならearly returnできるが、depthを返すと約束した以上、ダミーの値を返すのはやや抵抗感があった。

何日か脳内で寝かせてできたのがiterativeな解法。再帰をstackで表現することはわかったが、左右の結果が必要とのことでpost-order traversalをすることがしっくりくるまで数日要した。

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
    depth: int
    is_balanced: bool
```

を置いてみたが、あんまりいい抽象ができたようには思えなかった。結局`tuple`を見たら順番に意味があるのだとPythonに慣れている人なら理解するし、難しいことはせず必要ならコメントを残せばわかりやすいと思う。
	- 昔、プロジェクトの先輩に、コメントは更新忘れとかがあるから過信せず、コメントを残すくらいならとにかく実際の実装をわかりやすくするべき、という指摘を受けた記憶が蘇ってくる。

# Step 3

## ミスしたところ

- helper関数呼び忘れ
