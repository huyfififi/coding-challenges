# Step 1

## Step 1 - 1: slow runnerとfast runnerを用いる方法

Cracking the Coding Interviewでやったので知識として知っていた解法。一回の操作で1つ進むポインタと2つ進むポインタを用意して、　cycleが存在するならいつかは速い方のポインタが遅いポインタに追いつく。この方法なら、訪れたNodeをメモする必要がない。

## Step 1 - 2: 訪れたNodeをメモする方法

訪れたNodeをsetに保存していって、同じNodeに2回目訪れることになったらcycleがあると判定できる。この方法だとLinked Listの長さ分のメモリ空間が必要になるが、一番直感的で誰にとってもわかりやすい方法だと思う。

## Step 1 - 3: 問題の条件を利用する方法

Constraintsに

> The number of the nodes in the list is in the range [0, 10^4]

とあるので、とにかく前に進んで、cycleがないと仮定したLinked Listの長さが 10^4 を超えたら矛盾なのでcycleがあると返す。

# Step 2

## Cracking the Coding Interviewの読み返し

Cracking the Coding Interviewに載ってる問題は、単純なloop detectionではなく、loopが始まる場所を返せ、との問題設定だった。

ループではないところの長さが k、ループの長さが l だとする。

遅い方のポインタがk進んでループが始まる位置にいるとき、速い方のポインタはループが始まる位置から既に (k mod l) 進んでいる (i.e., ループの始点の l - k mod l 後ろにいる)。

そこから l - k mod l 遅いポインタが進み、速いポインタも 2 * (l - k mod l) 進めば2つが合流する。

今、ループの始点から l - k mod l 進んだ位置にいるので、その点からまたk進めば ((l - k mod l) + k) mod l = 0 でループの始点に行ける。
k進むには、片方をheadから、もう片方を合流点から1ステップずつ進める。

Floyd's cycle-finding algorithmという名前があるらしい。どれくらい一般常識なのだろうか。