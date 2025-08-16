# 20. Valid Parentheses
# Link: https://leetcode.com/problems/valid-parentheses/
# Difficulty: Easy
# Tags: String, Stack

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()
        return not stack
