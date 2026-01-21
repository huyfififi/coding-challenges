# Step 1

Cracking the Coding Interviewで取り組んだ記憶がある。

Binary Search Treeならもっと簡単な方法があるように思ったが、そのような制約はなさそうなので、root, p, q の位置関係で確認していくしかないかなと思った。

lowestではないancestorだったらpとqの両方が左右どちらかの部分木にいる。pとqが左右に散ったところがlowest common ancestor。
