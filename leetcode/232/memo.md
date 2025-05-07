# Step 1

FILOのStack一つだけでFIFOのQueueを実装できるとは思えないので、Stackを二つ使用することを考えた。In hindsight, 問題のタイトルが「Implement Queue using Stacks」とStackが複数形だったので、複数のStackを用いることは仄めかされていた。

2つのStackを用意し、片方の底をQueueの先頭、もう片方の底をQueueの末尾とすればうまくいきそう。

Queue: [1, 2, 3, 4]

| 4 |
| 3 |
| 2 |
| 1 |  |   |
|___|  |___|

Queueの末尾にPushの時は全ての要素をQueueの先頭側に寄せて、その上に乗せる。

                    | 5 |
| 4 |               | 4 |
| 3 |               | 3 |
| 2 |               | 2 |
| 1 |  |   |        | 1 |   |   |
|___|  |___|   ->   |___|   |___|

Queueの先頭からPopする時は、全ての要素をQueueの末尾側に移して、そこから値を取る。

        | 1 |
        | 2 |               | 2 |
        | 3 |               | 3 |
        | 4 |               | 4 |
|   |   | 5 |       |   |   | 5 |
|___|   |___|   ->  |___|   |___|

push か (pop または peek) が連続して呼ばれているとき、Stack内の要素の移し替えが発生せず、どちらかの一番上にアクセスするだけで良いので O(1)。
逆に、pushの次に (pop または peek)か呼ばれるとき (また、pop/peekの次にpushの場合)、仮想Queue内要素数(nとする)分移し替えが発生するので、O(n)。

償却計算量の分析として、n回の操作のうち、最初の(n-a)回はO(1)で、残りのa回はO(n)の操作が必要だと見積もると、総操作回数はだいたい

(n - a) * 1 + a * n = n - a + a * n

n回の操作の平均を取ると

(n - a + a * n) / n = 1 - a/n + a

aが定数の場合、この式は定数に収束するため、償却計算量はO(1)となる。
aがnに対して無視できない大きさ (例えばa = n/2など) の場合、償却計算量はO(n)となる。

償却計算量の見積もりをどのように展開すれば良いのかわからないので、他の方々のPRを見ることにする。

迷ったところは、二つのStackの命名で、どういう変数名がわかりやすいか少し考えてみたけれど、良い案が思い浮かばなかった。

## 別解 (`step1_b.py`)

少しChatGPTとやりとりしてみると、Queueを

Queue: [1, 2, 3, 4]

input   output

| 4 |   | 1 |
| 3 |   | 2 |
|___|   |___|

と表現する方法なら、私の方法よりも少ない操作回数で同じメソッドを実装できるよう。
実装してみると、確かに、peek/popにおいてoutputに使用するStackが空だった場合のみ移し替えが発生するので、操作の回数がかなり省けている。
このメモを書いている時点では、私の方法の方がQueueが今どのような状況なのか説明しやすく直感的にわかりやすいと思うが、少し脳内で寝かせてみることにする。

# Step 2

## [colorboxさんのPR](https://github.com/colorbox/leetcode/pull/15)

### 発見

- Queueの並びを保持するStackと、それを崩さないための待避用Stackというコンビネーションは思いつかなかった。確かにこの設定なら誰に対しても説明しやすいように感じる。
- peekとpopで似たような処理をするので、pop()内でpeek()をすることで共通化されている。

### 純粋関数型言語におけるQueueの実装

純粋関数型言語がcolorboxさんのPR上で言及されていたので軽くHaskell、QueueあたりでGoogle検索したら次のStackOverflowが出てきた。
[StackOverflow - Efficient queue in Haskell](https://stackoverflow.com/a/1740603/16193058)

> Alternatively, a well-known implementation of a purely functional queue is to use two lists. One for enqueue and another for dequeue.
> Enqueue would simply cons with the enqueue list. Dequeue takes the head of the dequeue list.
> When the dequeue list is shorter than the enqueue list, refill it by reversing the enqueue list.
> See [Chris Okasaki's Purely Functional Datastructures](https://www.cs.cmu.edu/%7Erwh/students/okasaki.pdf).

OdaさんがcolorboxさんのPRに残したPDFのリンクと同じものに辿り着いた。

> A common representation for purely functional queues [Gri81, HM81, Bur82] is as a pair of lists, F and R, where F contains the front elements of the queue in the correct order and R contains the rear elements of the queue in reverse order.

なるほど。業界でこの実装が有名ならば、「実装が直感的に説明できるか」を深く考えず、こちらの実装を頭に入れておいた方が良さそうだ。

Banker's Method: 実際にはかかっていない計算量をかかったとみなして貯金し、必要に応じてそれを使う。

今回の問題の例では、

push() -> 実際には操作は1回だが、2回としておく
pop() -> 基本的には1回。rearのstackが空の時、frontのstackからmの要素を移してくるのだが、frontにm個要素がある -> 既にpush()がm回呼ばれている -> mの貯金があるので、それを使用して1回の操作とみなせる。

そうすると、全てならして、時間計算量はO(1)になる。

面白い勉強になった。とにかくこの問題は、有名な実装に従ってStep 2、Step 3を作成しよう。

# Step 3

個人的には、pop()とpeek()の共通化はあまりしっくりとこなかった。なぜなら共通化をすると、pop()を読むときにpeek()(かもしくは値の移し替え用の共通メソッド)を確認しなければならず視線が移り意識が中断される。これくらいの行数なら書き下した方が読みやすいと思った。
