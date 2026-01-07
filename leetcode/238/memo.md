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

# Step 2

LeetCodeのSolutionsを眺めての自分なりの理解。

```python
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        products_except_self = [None] * len(nums)

        prefix_product = 1
        for i in range(len(nums)):
            products_except_self[i] = prefix_product
            prefix_product *= nums[i]

        suffix_product = 1
        for i in range(len(nums) - 1, -1, -1):
            products_except_self[i] *= suffix_product
            suffix_product *= nums[i]

        return products_except_self
```

step 1 で使用した例の

```
input:	[1, 2, 3, 4]
prefix: [1, 1, 2, 6]
suffix: [24, 12, 4, 1]
answer: [24, 12, 8, 6]
```

を思い出すと、ある要素の答えを出すとき、prefix/suffix product arrayの縦の列しか用いない。なので

```
products_except_self[i] = prefix_products[i] * suffix_products[i]
```

に集中できる。そこでまず

```
products_except_self[i] = prefix_products[i]
```

として、そのあと

```
products_except_self[i] *= suffix_products[i]
```

とすれば答えが求まる。そして、この方法なら全ての`prefix/siffix_products[i]`を保持する必要がないので、output に用いた `list` を除けば O(1)の空間計算量になる。

この解法はfollow upとあるので、時間が余ったら触れるくらいのもので、普通に面接をする分には素直にprefix and suffix products を持つ方法で十分なのだと予想するが、どうだろう。
一応、理解を深めるためにも練習しておくか。

# Step 3

左から右への走査と右から左への走査が意外とこんがらがってしまう。
