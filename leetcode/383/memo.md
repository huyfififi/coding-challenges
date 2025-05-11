# Step 1

必要な文字カウントと、与えられている文字カウントを出して比較。

`n = len(ransomNote)`, `m = len(magazine)`として、時間計算量は O(n + m)、空間計算量は O(1)、入力の文字列がEnglishのlowercaseしかないため。

Pythonのcollectionsは便利な関数が揃っているが、どこまでが知っておくべきものなのかは少し悩みどころ。
将来的に他の文字もサポートすることを考えると、素直に`Counter`、`defaultdict`、または`dict`を使用する方法が良さそうだが、本当にinputがEnglish lowercaseしかないならば、`list`にcountを持つアプローチの方が空間計算量が O(1) であることがわかりやすいと感じる。