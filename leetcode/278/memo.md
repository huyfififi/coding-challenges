# Step 1

1から順に確認していけば O(n) でできるが、Binary Searchを使えば O(log(2)n) で済むなというのはすぐに思いついた。

[git-bisect](https://git-scm.com/docs/git-bisect)という、Binary Searchでbugを探すコマンドを知っていたので、まんまだな、と思った。

> git-bisect - Use binary search to find the commit that introduced a bug

Binary Searchの変化形はいまだに、完全にはしっくり頭に収まらないが、一旦前に進むことにする。
