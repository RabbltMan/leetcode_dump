class Solution:
    def isValid(self, s: str) -> bool:
        tags = {'(': None, '[': None, '{': None, ')': '(', ']': '[', '}': '{'}
        stack = []
        for char in s:
            if stack and stack[-1] == tags[char]:
                stack.pop()
            else:
                stack.append(char)

        return not stack
