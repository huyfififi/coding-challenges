class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        appeared_num = set()
        for num in nums:
            if num in appeared_num:
                return True
            appeared_num.add(num)
        return False
