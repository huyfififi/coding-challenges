# Step 1

## DFS (`step1_dfs.py`)

Union Find が使えそうだなという直感はあったが、Union Find に明るくなく実装の方針が立たなかったので、同じアカウントのメールアドレス同士がedgeで繋がっているグラフだと見立ててDFSする方法で実装。
グラフと見立てることを思いつくのにかなりの時間を費やしてしまった。そういえばどこかでプログラミングコンテストの人が、グラフ問題に落とし込めれば大体の問題が解ける、とか言っていたような記憶があるが、具体的に思い出せないし少しGoogleしてもそれっぽいのはヒットしなかった。
また、ロジックとしては後から見返すと単純なのだが、コード自体は今まで取り組んだ中で一番長いものになってしまい、細かなtypo・データのミスマッチが増え、ちゃんと動くものが出来上がるまでかなり時間がかかってしまった。

## Union Find (`step1_union_find.py`)

DFSの実装の後、問題への理解も深まったので、Union Findを記憶から掘り起こしてみる。覚えているのは、各要素が自分のグループの代表を知っていることと、効率化策としてpath compressionとサイズが小さい方を大きい方のグループにmergeしていくこと。
一応動く形にはなったが、Union Findのクラスをgenericなものに留めて、他の場合にも再利用可能な形にすることができなかった。メールアドレスのダブりがあるので、単純にグループのサイズを足し算することができず、他に必要な関数も考えると、Accounts Mergeの問題設定に依存したものにならざるを得ないように思った。しかし、どこまでUnion Findクラスにロジックを吸収させるかもかなり迷って、うまくクラス間の責任の線引きができていないなと思いつつ、今出せるアウトプットとしてはこれが限界だった。

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
