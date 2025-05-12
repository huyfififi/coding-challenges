# Step 1

自分で手作業でやるとしたら、まず必要な文字の数を数えてメモ、次に使える文字の数を数えてメモ、最後に必要な文字分使える文字があるかどうか確認、かなと思い実装。

`n = len(ransomNote)`, `m = len(magazine)`として、時間計算量は O(n + m)、空間計算量は O(1)、入力の文字列がEnglishのlowercaseしかないため。

Pythonのcollectionsは便利な関数が揃っているが、どこまでが知っておくべきものなのかは少し悩みどころ。
将来的に他の文字もサポートすることを考えると、素直に`Counter`、`defaultdict`、または`dict`を使用する方法が良さそうだが、本当にinputがEnglish lowercaseしかないならば、`list`にcountを持つアプローチの方が空間計算量が O(1) であることがわかりやすいと感じる。

# Step 2

[rihibさんのPR](https://github.com/rihib/leetcode/pull/34)
    - なるほど、counterを一つだけにして、magazineで+、ransomNoteで-する方法もあったか。あとでやってみよう。
[Kitaken0107さんのPR](https://github.com/Kitaken0107/GrindEasy/pull/28)
[NobukiFukuiさんのPR](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/26)
    - 上のお二方と同様、magazineで+、ransomNoteで-していくやり方。
[colorboxさんのPR](https://github.com/colorbox/leetcode/pull/17)

言われてみれば、使える文字の数を数えてメモし、次に使用する文字を見つけてはメモにある数を減らしていく方法の方が少ない手間で済むか。

# Feedback

小文字以外が入力される場合のこと（拡張性）も念頭に置くように
