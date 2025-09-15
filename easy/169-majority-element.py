# 169. Majority Element
# Link: https://leetcode.com/problems/majority-element/
# Difficulty: Easy
# Tags: Array, Sorting, Divide and Conquer

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        length = len(nums)

        if length % 2 == 0:
            n = length // 2
        else:
            n = (length + 1) // 2 - 1

        if n >= len(nums):
            return nums[0]

        return nums[n]
    