# Step 1

Google 画像検索ででてきたTrieの画像を見て実装した。

# Step 2

LeetCodeのSolutionsと一例だけあったDiscord内のPRを眺めてみると、各ノードに値をもたず、childrenのmap + 単語終わりを表すフラグ で実装されていた。確かに、各ノードに値を持たなくてもTrieの構造を表現、特に今回の問題の要件を満たせているので、`TrieNode`の`letter` (childrenとフラグ以外の値) は不要だった。
