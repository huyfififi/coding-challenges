# Step 1

全ての数字を掛け合わせて、selfで割っていけばいいじゃ〜んと思ったのも束の間、

> without using the division operation.

と問題文にあるのを見つけて意気消沈。愚直にループを回すとO(n^2)の解法ができるが、

> You must write an algorithm that runs in O(n) time

とあるので、これもダメ。なんらかのデータ構造を持って、計算を短縮するのだろうという予想はつくが、何も思いつかなかった。

> The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

とあり、Hint 1 を覗いてみても prefix and suffix products を利用せよと書いてあるので、色々こねくり回していたら

```
input:	[1, 2, 3, 4]
prefix: [1, 1, 2, 6]
suffix: [24, 12, 4, 1]
answer: [24, 12, 8, 6]
```

縦の列をみると、prefix product と suffix product の積が答えになっていることに気がついた。
(ここに至るまで、prefix sum arrayの問題みたいにinclusiveな、自分自身を積に含むarrayを考えていてかなり時間を費やした。)

確かに、

```
prefix[i] = nums[0] + nums[1] + ... + nums[i - 1]
suffix[i] = nums[i + 1] + nums[i + 2] + ... + nums[n]
```

の時、`prefix[i] * suffix[i]` は自分自身を除いた全ての数の積になる。

follow up に 出力を除いた空間計算量が O(1) の解法を、つまりprefix and suffix product arrays を保持しない解法を、というものがあったが、思いつかなかったので、Step 2 で他の方々の解法を見ようと思う。
