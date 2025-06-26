# Step 1

## fast runner と slow runner を用いる方法

[LeetCode 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)で用いたRobert W. Floyd's tortoise and hare algorithmがすぐに連想された。

1回に1つ動くslow runnerと、1回に2つ動くfast runnerを走らせて、fast runnerが末尾に着いたら、1/2の速さで動くslow runnerがlinked listの真ん中にいるはず。

## Linked Listの長さを測る方法

まず、一回Linked Listを走査して長さを測り、半分の長さがわかったら、二回目の走査で半分まで行ってそこのNodeを返す方法もあるなと考えた。
