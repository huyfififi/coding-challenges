class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix_products = [1]
        for num in nums[:-1]:
            prefix_products.append(prefix_products[-1] * num)

        reversed_suffix_products = [1]
        for num in reversed(nums[1:]):
            reversed_suffix_products.append(reversed_suffix_products[-1] * num)
        suffix_products = reversed(reversed_suffix_products)

        return [pp * sp for pp, sp in zip(prefix_products, suffix_products)]
