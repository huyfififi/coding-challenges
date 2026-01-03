# Step 1

有向グラフ (directed graph) を考えた時に、cycleがあればfalse、なければtrueだと考えた。
愚直に全てのノードからDFSしていってcycleがないことを確認する方法に加えて、Topological Sortも連想された。
とりあえず両方実装してみたが、Topological Sort (の派生、実際に順序を出力するわけではないので) の方は一般的な実装方法に沿っている自信がない。また、DFSの解法で、他に良い案も思いつかなかったのでvisiting/visitedという言葉を使ったが、いきなりグラフを設定していて問題文の語彙からややかけ離れているような抵抗感があった。

# Step 2

Wikipediaを眺めると、私がトポロジカルソートだと思っていたアルゴリズムはトポロジカルソートの中でも特にKahn's algorithmと呼ばれるもので、それとは別にDFSを用いる方法もあるよう。やや掲載されている擬似コードと私の実装は異なるか。

Discord内で前例が少なかったので、一応LeetCodeのSolutionsも眺めてみたが、変数・関数名が読み取りづらかったのと、queue + indegree count を用いる方法は一旦しっくりこなかったので飛ばした (追記: queueとindegree countを用いる方法も書いてみたが、こちらの方がわかりやすい気がする `step2_kahn.cpp` から `step2_more_bfs_like.cpp` へ)。

`HasCycle()`としているのに、cycle detectionだけでなく他のデータ変更もしているのが気になるが、他に良いメソッド名が思いつかなかった。

# Step 3

Mistakes:

- pass by reference
- type syntax
- last return value

3回繰り返したらqueueを用いる方法 (`step3_bfs_based.cpp`) がしっくりきた。

自分のstep 1/2のKahn's algorithmの回答を見返してみると、keyがない -> visited、valueがempty -> visiting、valueがnon empty set -> unvisited であることがコメントなしだと伝わりにくく感じ、素直にindegree countsを持つ方が読み取りやすく感じた。
