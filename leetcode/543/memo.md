# Step 1

## Diameter of Binary Treeの理解

問題文を読んで、少し脳内でいくつか例を考えて見た結果、"diameter of binary tree"は`root`において (左の部分木の高さ) + (右の部分木の高さ)ではないかと考えた。しかし、いざ走らせてみると、パスしないテストケースが見つかった。
テストケースを見てよく考えてみると、diameterとなるpathはrootを経由しない場合もあり得るな、と気づいた。

## max depth vs height

[LeetCode 104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/)が脳内にちらついていたので、`max_depth`という見方をしていたが、`height`の方が端的に木の高さを表せて良いな、と`step1_recursive.py`の後考えた。

```
height = max depth (depth of the deepest node(s))
```

# Step 2

## 先駆者の方々のPR

- [Jikuharaさん](https://github.com/Jikuhara/LeetCode/pull/5)
- [NobukiFukuiさん](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/36)
	- `calculate_diameter_and_depth`という命名いいな、真似しよう
- [Kitaken0107さん](https://github.com/Kitaken0107/GrindEasy/pull/17)
