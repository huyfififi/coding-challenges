# Step 1

再帰関数の方は特に引っかかることもなく書けた。左右片方でも既にアンバランスならearly returnできるが、depthを返すと約束した以上、ダミーの値を返すのはやや抵抗感があった。

Iterativeに書こうとして、詰まって、ChatGPTにひとつだけヒントをくれとお願いして、各nodeの結果を保持する`dict`を持つと良いと言われ、多大な時間をかけてできたのが`step1_iterative.py`。`dict`を持たずとも`tuple`を拡張するかクラスを定義してcall framesを模すことでも実装可能なよう（？要出典）だが、今の私が現実的な時間内に再現可能になるかは微妙なので一旦忘れることにする。

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