# Step 1

## DFS (`step1_dfs.py`)

Union Find が使えそうだなという直感はあったが、Union Find に明るくなく実装の方針が立たなかったので、同じアカウントのメールアドレス同士がedgeで繋がっているグラフだと見立ててDFSする方法で実装。
グラフと見立てることを思いつくのにかなりの時間を費やしてしまった。そういえばどこかでプログラミングコンテストの人が、グラフ問題に落とし込めれば大体の問題が解ける、とか言っていたような記憶があるが、具体的に思い出せないし少しGoogleしてもそれっぽいのはヒットしなかった。
また、ロジックとしては後から見返すと単純なのだが、コード自体は今まで取り組んだ中で一番長いものになってしまい、細かなtypo・データのミスマッチが増え、ちゃんと動くものが出来上がるまでかなり時間がかかってしまった。

## Union-Find (`step1_union_find.py`)

DFSの実装の後、問題への理解も深まったので、Union-Findを記憶から掘り起こしてみる。覚えているのは、各要素が自分のグループの代表を知っていることと、効率化策としてpath compressionとサイズが小さい方を大きい方のグループにmergeしていくこと。
一応動く形にはなったが、Union-Findのクラスをgenericなものに留めて、他の場合にも再利用可能な形にすることができなかった。メールアドレスのダブりがあるので、単純にグループのサイズを足し算することができず、他に必要な関数も考えると、Accounts Mergeの問題設定に依存したものにならざるを得ないように思った。しかし、どこまでUnion-Findクラスにロジックを吸収させるかもかなり迷って、うまくクラス間の責任の線引きができていないなと思いつつ、今出せるアウトプットとしてはこれが限界だった。

# Step 2

## DFS

LeetCodeのSolutionsを眺めてみて気づいたのは、私がemail -> all alternatives のmapを作っていたのに対して、全てのDFSの解法が、DFSが行える最低限のグラフの構築に留めていたことだった。
例えば、kazuki1@gmail.com, kazuki2@gmail.com, kazuki3@gmail.comという同じアカウントのメールアドレスがある場合、私のstep 1 の解法だと

kazuki1@gmail.com -> kazuki2@gmail.com, kazuki3@gmail.com
kazuki2@gmail.com -> kazuki1@gmail.com, kazuki3@gmail.com
kazuki3@gmail.com -> kazuki1@gmail.com, kazuki2@gmail.com

を作成するのに対して、他の方々の解法は

kazuki1@gmail.com -> kazuki2@gmail.com, kazuki3@gmail.com
kazuki2@gmail.com -> kazuki1@gmail.com
kazuki3@gmail.com -> kazuki1@gmail.com

などとして、DFSできるなら全ての経路をカバーする必要はないとしている。大きくオーダーには影響しなさそうだが、DFSで検討すべきedgeの数も、グラフ構築のループも減らせる。

あとは、大体私と同じようなロジックのように見受けられる。

書いてみたが (-> `step2_dfs.py`) 、グラフ理論(?)が前提となる名付けしか思いつかなかった。

## Union-Find

Discord内でOdaさんの説明があった

- [https://discord.com/channels/1084280443945353267/1084283898617417748/1296133905723822153](https://discord.com/channels/1084280443945353267/1084283898617417748/1296133905723822153)
- [https://discord.com/channels/1084280443945353267/1183683738635346001/1197738650998415500](https://discord.com/channels/1084280443945353267/1183683738635346001/1197738650998415500)

Wikipediaを覗くと [https://en.wikipedia.org/wiki/Disjoint-set\_data\_structure](https://en.wikipedia.org/wiki/Disjoint-set_data_structure)

> It provides operations for adding new sets, merging sets (replacing them with their union), and finding a representative member of a set.

とある。初期化のメソッド、find()、union() があれば Union-Find と呼んでも差し支えないのかな。

と考えると、`step1_union_find.py`では非常に煩雑な実装になってしまっていたが、`__init__()__`, `find()`, `union()` だけを持つ `UnionFind`クラスを定義すればもっと単純な実装になりそうだな。
