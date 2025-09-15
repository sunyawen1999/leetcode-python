# 75. Sort Colors
# Link: https://leetcode.com/problems/sort-colors/
# Difficulty: Medium
# Tags: Array, Two Pointers, Sorting

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # 重新填充数组
        for i in range(count.get(0, 0)):
            nums[i] = 0
        for j in range(count.get(1, 0)):
            nums[count.get(0, 0) + j] = 1
        for k in range(count.get(2, 0)):
            nums[count.get(0, 0) + count.get(1, 0) + k] = 2
