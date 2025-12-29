# Step 1

大学で逆ポーランド記法を習っていたので、解法は知識として知っていた。

operatorsを最初の定数と条件式で各2回書いているのが、どちらかを間違えて書いてしまった場合にバグが起こるので嫌だなぁと思ったが、代替案も思いつかないのでこの形のままにした。

`+`, `-`, `*`, と`/`を処理する条件式が並列であることを強調するため、`if`ではなく`switch`を用いようとしたが、`std::string`はそのまま`switch`に用いることができなかった。

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

# Feedback

- 要素数が十分小さい場合は、線形探索した方がはやくなる場合がある。

```python
import time


s = {(i + 1) for i in range(100)}
l = [(i + 1) for i in range(100)]

iterations: int = 100000000

start = time.time()
for i in range(iterations):
    result: bool = 1 in s
end = time.time()
print(f"1 in set - {end - start}")

start = time.time()
for i in range(iterations):
    result: bool = 1 in l
end = time.time()
print(f"1 in list - {end - start}")

start = time.time()
for i in range(iterations):
    result: bool = 10 in s
end = time.time()
print(f"10 in set - {end - start}")

start = time.time()
for i in range(iterations):
    result: bool = 10 in l
end = time.time()
print(f"10 in list - {end - start}")

start = time.time()
for i in range(iterations):
    result: bool = 100 in s
end = time.time()
print(f"100 in set - {end - start}")

start = time.time()
for i in range(iterations):
    result: bool = 100 in l
end = time.time()
print(f"100 in list - {end - start}")

"""
1 in set - 6.646394968032837
1 in list - 6.620666027069092
10 in set - 6.6902382373809814
10 in list - 9.636014223098755
100 in set - 6.710673093795776
100 in list - 41.18491005897522
"""
```

- `bool kOperatorChars[256];`を定義し、`+-*/`だけtrueにして、tokenの1文字目で判断する高速化案もある。
