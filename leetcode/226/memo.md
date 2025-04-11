# Step 1

## 解法1. 入力文字列をソートして比較

- Time Complexity: O(nlogn) (ソートのため)
- Space Complexity: O(n) (新しい文字列を作っているため)

- 解法1. 入力文字列をソートして比較
	- Time Complexity: O(nlogn) (ソートのため)
	- Space Complexity: O(n) (新しい文字列を作っているため)
- 解法2. Arrayに各文字の個数をカウントして比較
	- Time Complexity: O(n) (文字列をiterateするため)
	- Space Complexity: O(1) (Arrayの長さは26で固定のため)
- 解法3. Hash Tableで各文字の個数をカウントして比較
	- 解法2では入力にlowercaseのalphabetを想定しているが、文字一般をサポートすることができない。
	- Time Complexity: O(n) (文字列をiterateするため)
	- Space Complexity: O(n) (ユニークなcharacterの最大数n, Unicode charactersをサポートする場合)
