# Step 1

len(s)をn、len(t)をmとすると

- 解法1. 入力文字列をソートして比較
	- Time Complexity: O(nlogn + mlogm) (各文字列もソートするため)
	- Space Complexity: O(n + m) (ソートによって新しい文字列を作成するため)
- 解法2. Arrayに各文字の個数をカウントして比較
	- Time Complexity: O(n + m) (1回ずつ文字列を走査するため)
	- Space Complexity: O(1) (配列のサイズはアルファベット26文字で固定のため)
- 解法3. Hash Tableで各文字の個数をカウントして比較
	- 解法2では入力にlowercaseのalphabetを想定しているが、文字一般をサポートすることができない。
	- Time Complexity: O(n + m) (1回ずつ文字列を走査するため)
	- Space Complexity: O(n + m) (ユニークな文字が最大でn種類ある場合)
