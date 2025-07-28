# 412. Fizz Buzz
# Link: https://leetcode.com/problems/fizz-buzz/
# Difficulty: Easy
# Tags: Array, String, Simulation

from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = ["0"] * n
        for i in range(n):
            if (i+1) % 3 == 0 and (i+1) % 5 == 0 :
                ans[i] = "FizzBuzz"
            elif (i+1) % 3 == 0:
                ans[i] = "Fizz"
            elif (i+1) % 5 == 0:
                ans[i] = "Buzz"
            else:
                ans[i] = str(i+1)
        return ans