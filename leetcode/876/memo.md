# Step 1

## fast runner と slow runner を用いる方法

[LeetCode 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)で用いたRobert W. Floyd's tortoise and hare algorithmがすぐに連想された。

1回に1つ動くslow runnerと、1回に2つ動くfast runnerを走らせて、fast runnerが末尾に着いたら、1/2の速さで動くslow runnerがlinked listの真ん中にいるはず。
