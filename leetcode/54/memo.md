# Step 1

方針はすぐに立ち、実装も特に問題を感じなかった。
右・下・左・上の順で、端まで進み、方向を変える。方向を変えても進めなかったら最後まで行ったということなので、ループを終える。
方向を変えた先が探索可能かのチェックには、`remaining_cell_count` を持って、`0` になったら `return` するのでもよかったかも。

一つミスしたのは、`visited[row][col] = True` を忘れて無限ループに陥っていたこと。

# Step 2

[thonda28さんのPR](https://github.com/thonda28/leetcode/pull/13/changes)

なるほど、一周 (右方向・下・左・上) を一区切りとして、だんだん内側に狭めていく方法だ。
私の、`visited` や 境域チェック関数 などのやや煩雑な設定がなくて、シンプルだな。

[CodingNinjaさんのLeetCode上のSolution](https://leetcode.com/problems/spiral-matrix/solutions/5513240/video-explanation-by-niits-1mqh)

90度曲がることを

```python
x, y, dx, dy = 0, 0, 1, 0

```
dx, dy = -dy, dx
```

のように表現している。言われてみれば確かに、方向転換のロジックが簡潔に示せて綺麗な書き方だ。

2次元平面上の点を回転させる行列が

```
cosθ, -sinθ
sinθ, cosθ
```

で、`θ = 90°` の時、`col, row = col * cos90° - row * sin90°, col * sin90° + row * cos90° = -row, col` (`x = col`, `y = row` と置くとき)。
なので、deltaをそのように更新していけば、方向転換が表現できる。
また、終了判定を処理したセルの数で見ていて、シンプルなfor文で表現できている。

こうしてみると、私の解法は、何をやろうとしているのかは明確な？ものの、かなり煩雑な処理になってしまっているか？

C++ で書いてみたが、なかなか長くなってしまうな。

```
dx, dy = -dy, dx
```

が簡潔に表現できなかったり、`0 <= row < num_rows` ができなかったり。
