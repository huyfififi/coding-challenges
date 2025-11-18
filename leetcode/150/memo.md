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

# Step 2

Discord内では、この問題をC++で解かれた方は見当たらなかった。
