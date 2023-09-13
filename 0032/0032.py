class Solution:
    def longestValidParentheses(self, s: str) -> int:
        dp = [0] * len(s)
        for i, c in enumerate(s):
            if c == '(':
                continue
            elif (i > 0):
                if (s[i-1] == '('):
                    dp[i] = 2 + dp[i-2] if i >= 2 else 2
                elif (i-dp[i-1]-1 >= 0 and s[i-dp[i-1]-1] == '('):
                    dp[i] = 2 + dp[i-1] + dp[i-dp[i-1]-2]

        return max(dp) if dp else 0
