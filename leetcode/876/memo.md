# Step 1

## fast runner と slow runner を用いる方法

[LeetCode 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)で用いたRobert W. Floyd's tortoise and hare algorithmがすぐに連想された。

1回に1つ動くslow runnerと、1回に2つ動くfast runnerを走らせて、fast runnerが末尾に着いたら、1/2の速さで動くslow runnerがlinked listの真ん中にいるはず。

## Linked Listの長さを測る方法

まず、一回Linked Listを走査して長さを測り、半分の長さがわかったら、二回目の走査で半分まで行ってそこのNodeを返す方法もあるなと考えた。こちらの方法も、上の方法と同時に思いついた。

# Step 2

## 他の方々のPRを見てみる

- [NobukiFukuiさん](https://github.com/NobukiFukui/Grind75-ProgrammingTraining/pull/37)
	- 確かに、真ん中まで移動するカウントの変数名をどうするかは、議論されている通りに迷った。
	- 解法のバリエーションは私のStep 1と同じ。
- [rihibさん](https://github.com/rihib/leetcode/pull/40)
	- 長さを数える方法の方が素直らしい。

## その他

`move_count_to_middle`という変数名の代替案を考えていたが、上手いものが思いつかなかった。`middle_index`は、0から始まるのか1から始まるのか、わかりづらい気がするし...。
