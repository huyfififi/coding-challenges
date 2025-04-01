# Step 1

## 感想

一見簡単に見えたが、行数が増えreferenceの処理が絡むとバグのないコードを書くのがかなり難しく感じ、とりあえずテストケースをパスするコードは書けたものの、かなり読みにくいものになってしまった。コーディングをもう一度学び直すような心持ちで取り組もうと思った。

# Step 2

## Step 1の間に考えたこと

- 同じような処理をlist1とlist2を入れ替えただけで2回行っており、typoや書き忘れのバグが起きる確率が（厳密ではない議論として）単純に2倍になっているのではないかと思った。list1とlist2は入れ替えても問題がなく順序や優劣がないので、共通のfunctionを書いて使いまわせないか、と考えた。単純な操作を2回繰り返しているだけなので、わざわざ関数で包んでしまうと逆にわかりづらくなるような懸念もある。
- referenceの操作が多く頭がこんがらがりがちなので、どこか回数を減らせる（？）操作があればシンプルにしたいと思った。
- 再帰的なアプローチは大きな課題を分割し1つのステップに集中できるので綺麗に書けるかと思いきや、個人的にはループ処理の方がわかりやすいなと思った。関数型言語に明るい友人も、結局簡単なロジックならループの方がわかりやすいと言っていたのを思い出した。

## 他の方々のPRを見て

- [azriel1rfさん](https://github.com/azriel1rf/leetcode-prep/pull/6)
	- `dummy = ListNode()`を作ることでhead周りの処理を省くことができている。
	- PEP8に"Also, beware of writing if x when you really mean if x is not None – e.g. when testing whether a variable or argument that defaults to None was set to some other value."とあり、azriel1rfさんは`is not None`と明記していた。[Google Python Style Guide](https://google.github.io/styleguide/pyguide.html)でも"Always use if foo is None: (or is not None) to check for a None value."とあるので、こちらに従おうと思う。
- [kzhraさん](https://github.com/kzhra/Grind41/pull/3)
	- [odaさんのコメント](https://github.com/kzhra/Grind41/pull/3#discussion_r1597538900)が私にない意見だったので興味深かった。

他の方々のPRもいくつか流し見したが、step 1の間に考えた可換な処理を抜き出すことは逆にコードを複雑にしそうだと思った。
