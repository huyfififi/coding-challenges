# Step 1

有向グラフ (directed graph) を考えた時に、cycleがあればfalse、なければtrueだと考えた。
愚直に全てのノードからDFSしていってcycleがないことを確認する方法に加えて、Topological Sortも連想された。
