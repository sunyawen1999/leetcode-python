# 35. Search Insert Position
# Link: https://leetcode.com/problems/search-insert-position/
# Difficulty: Easy
# Tags: Array, Binary Search

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n - 1
        if target > nums[-1]:
            return n
        elif target <= nums[0]:
            return 0 
        else:
            for i in range(n):
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
        return mid