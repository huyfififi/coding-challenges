# Step 1

1から順に確認していけば O(n) でできるが、Binary Searchを使えば O(log(2)n) で済むなというのはすぐに思いついた。

[git-bisect](https://git-scm.com/docs/git-bisect)という、Binary Searchでbugを探すコマンドを知っていたので、まんまだな、と思った。

> git-bisect - Use binary search to find the commit that introduced a bug

Binary Searchの変化形はいまだに、完全にはしっくり頭に収まらないが、一旦前に進むことにする。

assertを入れたのは、while文から抜けたら`left_i == right_i`になっているはずだ、ということを読み手に共有、また、自分だったら、`right_i`だけ返されているのを見ると、`left_i`ではいけない理由を考えてしまうため、`right_i == left_i`の関係であるとすぐ上で明記されるとわかりやすい気がするため。

# Step 2

- [rihibさんのPR](https://github.com/rihib/leetcode/pull/33)
    - `isBadVersion()`が重たい処理である可能性がある、という観点が私から抜けていた。
- [NobukiFukuiさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/25)
- [colorboxさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/25)
    - Pythonでは気にしなくてもいいが、溢れないように`int mid = left + (right - left) / 2;`とする方法は覚えておこうと思う。

やはり閉区間・半開区間を切り替えた場合の扱いが難しいが、一旦自分のわかりやすい閉区間で先に進み、頭の中で寝かせておくことにする。
