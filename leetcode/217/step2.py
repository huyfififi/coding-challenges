class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        appeared_nums = set()
        for num in nums:
            if num in appeared_nums:
                return True
            appeared_nums.add(num)
        return False
