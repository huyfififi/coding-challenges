# Step 1

## Step 1 - 1: slow runnerとfast runnerを用いる方法

Cracking the Coding Interviewでやったので知識として知っていた解法。一回のループで1つ進むポインタと2つ進むポインタを用意して、　cycleが存在するならいつかは速い方のポインタが遅いポインタに追いつく。この方法なら、訪れたNodeをメモする必要がない。

## Step 1 - 2: 訪れたNodeをメモする方法

訪れたNodeをsetに保存していって、同じNodeに2回目訪れることになったらcycleがあると判定できる。この方法だとLinked Listの長さ分のメモリ空間が必要になるが、一番直感的で誰にとってもわかりやすい方法だと思う。

## Step 1 - 3: 問題の条件を利用する方法

Constraintsに

> The number of the nodes in the list is in the range [0, 10^4]

とあるので、とにかく前に進んで、cycleがないと仮定したLinked Listの長さが 10^4 を超えたら矛盾なのでcycleがあると返す。
問題の条件に依存しているので邪道であろう。

# Step 2

## Cracking the Coding Interviewの読み返し

Cracking the Coding Interviewに載ってる問題は、単純なloop detectionではなく、loopが始まる場所を返せ、との問題設定だった。

ループではないところの長さが k、ループの長さが l だとする。

遅い方のポインタがk進んでループが始まる位置にいるとき、速い方のポインタはループが始まる位置から既に (k mod l) 進んでいる (i.e., ループの始点の l - k mod l 後ろにいる)。

そこから l - k mod l 遅いポインタが進み、速いポインタも 2 * (l - k mod l) 進めば2つが合流する。

今、ループの始点から l - k mod l 進んだ位置にいるので、その点からまたk進めば ((l - k mod l) + k) mod l = 0 でループの始点に行ける。
k進むには、片方をheadから、もう片方を合流点から1ステップずつ進めれば良い。

Floyd's cycle-finding algorithmという名前があるらしい。どれくらい一般常識なのだろうか。

## 他の方々のPRを見てみる

- [potrueさん](https://github.com/potrue/leetcode/pull/1)
    - どこかで合流したらcycleということに注目して私自身は`while slow is not fast:`というループ条件にしていたが、`while fast is not None and fast.next is not None:`としてcycleがないということに注目したループ条件もわかりやすいなと思ったし、ざっと本や他の方々のコードを見ると多くののコードがこれ（後者）だった。
- [nktr-cpさん](https://github.com/nktr-cp/leetcode/pull/2)
- [garunituleさん](https://github.com/garunitule/coding_practice/pull/1)
    - 私と同じくループ条件を`while slow is not fast:`にされている。
- [rieukyさん](https://github.com/rieuky/arai60/pull/1)
- [tokuhiratさん](https://github.com/tokuhirat/LeetCode/pull/1)

## もう一度振り返って

- コードの量自体は大したことないが、知識（経験）問題かもしれない。普通の人間が限られた時間内で0からslow_runnerとfast_runnerを使用する方法を思いつけるとは思えない。

- while文の条件は今回の場合あまり可読性に関わらなさそう。単に注目することを入れ替えているだけでコードも大きく変化しないので。

# Feedback

- 主役に据えるものを明確にすると良いかも。例えば、while文の条件を主役に添える変数にする。
- 変数の初期化とその処理の間にスペースを入れない形を好む方がいる。
- Floyd's cycle-finding algorithmは知識としてなんとなく知っていれば良い。
