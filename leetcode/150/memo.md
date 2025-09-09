# Step 1

この問題は、記憶が定かではないが学部の授業でやったような気がする。Reverse Polish Notationは演算子の優先順位を考えなくてもよく、Computer上ではStackで簡潔に処理できるので嬉しい、のような話だった気がするが

知識として知っていたので、C++のswitch構文やstring -> intの変換を調べつつ、とりあえず動く形になったのが `step1.cpp`。

```
if (token != "+" && token != "-" && token != "*" && token != "/")
```

という条件、Pythonだったら

```
if token not in ("+", "-", "*", "/"):  # またはtupleを別で定義するのもアリ
```

のようにできるのにな、と思ったが、とりあえず愚直に書き下す形で先に進み、次に他の方々のコードを見ることで感覚を養うことを試みることにする。

他にも、`token_stack.push(std::to_string()`が繰り返されていること、stackから取り出す2つの数字の変数名、stackの命名をどうするか (データ構造や型名を名前につけるのは情報が増えないのに変数名が長くなるので、`token_stack`ではなく`tokens`などとしたかったが、引数と被ってしまう。他の良い案も思いつかなかった) に悩んだ。

そういえば、問題の制約上起こり得ないが、C++で、0を数字で割ろうとするとどうなるんだろう。PythonだったらZeroDivisionErrorになるはず。後で調べてみよう。

# Step 2

## Division by zero

```cpp
#include <iostream>

int main() {
    int a = 1 / 0;
    std::cout << a << std::endl;
}
```

```zsh
$ g++ divide.cpp
divide.cpp:4:15: warning: division by zero is undefined [-Wdivision-by-zero]
    4 |     int a = 1 / 0;
      |               ^ ~
1 warning generated.
```

コンパイルしたら未定義動作？との警告が出た。

```zsh
$ ./a.out
75695256
$ ./a.out
9782424
$ ./a.out
6177944
$ ./a.out
82904216
$ ./a.out
14484632
$ ./a.out
73745560
```

毎回違う値が出てきているように見える。法則性も見つからない。

[nasal demons](http://www.catb.org/jargon/html/N/nasal-demons.html)という言葉があるらしい。

[Hacker News](https://news.ycombinator.com/item?id=8234013)

> ...when you hit undefined behavior, the compiler would be completely within its rights to make demons fly out of your nose.
> "Undefined behavior" means the compiler can do anything.

[cppreference.com - Undefined behavior](https://en.cppreference.com/w/cpp/language/ub.html)

> *undefined behavior* - There are no restrictions on the behavior of the program.

本当に何の保証もなく、何が起こってもおかしくないらしい。

## TODO: `const &`

## LeetCodeのSolutionsやLLMの提示する解法を流し見て

演算子か判定する関数を切り出す方法、演算子とlambdaのmapを作って条件分岐の代わりに用いる方法、switchを用いる方法などがあったが、どれもわかりやすさが向上しているようには思えなかった。演算子は基本的に今与えられている四つから大幅に増えることはないだろうと予想され、また各処理は簡潔で具体的な操作を隠せるメリットが目移りするデメリットを超えてこないように感じるので、素直にif文で書き下す方法が一番わかりやすいのではないだろうか。
