# Step 1

愚直にやれば、`s` の全ての substring に対して、`t` とマッチしているか判定すればいい

```py
for start in range(len(s)):
    for end in range(start + 1, len(s)):
	# convert s substring and t into counter and match
```

みたいな感じで `O(m ^ 2 * (m + n))` だろうか。制約から `1 <= m, n <= 10^5` なので、Python だと大体 `10 ^ 15 / 10 ^ 6 = 10 ^ 9 s` ほどかかってしまいそう。
