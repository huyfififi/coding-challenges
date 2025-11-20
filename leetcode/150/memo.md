# Step 1

大学で逆ポーランド記法を習っていたので、解法は知識として知っていた。

operatorsを最初の定数と条件式で各2回書いているのが、どちらかを間違えて書いてしまった場合にバグが起こるので嫌だなぁと思ったが、代替案も思いつかないのでこの形のままにした。

+`, `-`, `*`, と`/`を処理する条件式が並列であることを強調するため、`if`ではなく`switch`を用いようとしたが、`std::string`はそのまま`switch`に用いることができなかった。

[cppreference.com - switch statement](https://cppreference.com/w/cpp/language/switch.html)

> condition can only yield the following types:

> - integral types
> - enumeration types
> - class types

> If the yielded value is of a class type, it is contextually implicitly converted to an integral or enumeration type.

operatorであれば一文字であることがわかっているので、先にoperatorかどうか判定して、`char`を`switch`に用いればいいのだが、やや条件式が複雑になってしまう気がしたので避けた。

# Step 2

Discord内では、この問題をC++で解かれた方は見当たらなかった。

LeetCodeのSolutionsをざっと10つくらい眺めて、一つだけ有用そうで目に留まったのが、`std::plus`, `std::minus`, `std::multiples`, `std::divides`を用いる書き方だった。これなら`'+'`などを2回書かずに済んで、食い違いの確認の手間が省けるし、条件式もなくせそうだ。
