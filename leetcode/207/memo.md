# Step 1

有向グラフ (directed graph) を考えた時に、cycleがあればfalse、なければtrueだと考えた。
愚直に全てのノードからDFSしていってcycleがないことを確認する方法に加えて、Topological Sortも連想された。
とりあえず両方実装してみたが、Topological Sortの方は一般的な実装方法に沿っている自信がない。
