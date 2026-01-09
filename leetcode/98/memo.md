# Step 1

## Step 1 - 1

各nodeが、左のnodeと右のnodeからそれぞれ報告書をもらって、上のnodeに (自分がBSTの条件を満たしているか, 自分からなる部分木の最小値, 部分木の最大値) を返せば良いと思った。
左側を先にチェックして、BSTの条件を既に満たしていなかったら右側をチェックせずに切り上げる方法もあると思うが、やや例外的なロジックを足すより、(is valid BST, min, max) を絶対に返すと約束する方がシンプルで頭に収まりやすいように感じる (偏った感覚かも)。

## Step 1 - 2

レビュー依頼に流れてたPRを眺めていた時の記憶で、`lo`と`hi`を子nodeに送っていって取ってもいい値の幅を狭めていく方法もあった気がする。

## Step 1 - 3

step 1 - 2 を iterative に。

Pythonのrecursion limitはdefaultだと1000なので、それより深い木を扱うには自前でstackを用意する必要がある。(LeetCode上ではこの設定が上書きされているようだが。)

## Step 1 - 4

Binary Search Tree を inorder traversal するとincreasing (sorted) sequence になる。

## Step 1 - 5

step 1 - 4 を、わざわざ`list`で持たず都度確認する形にするとこうなりそう。
