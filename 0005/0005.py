class Solution:
    def longestPalindrome(self, s: str) -> str:
        strLength = len(s)
        if (strLength == 1):
            return s
        start, end, maxSubStringLength = 0, 0, 1
        isPalindrome = [[False for i in range(strLength)] for i in range(strLength)]
        right = 1
        while(right < strLength):
            left = 0
            while(left < right):
                if (s[left] == s[right] and (right-left <= 2 or isPalindrome[left + 1][right - 1])):
                    isPalindrome[left][right] = True
                    if (right - left + 1 > maxSubStringLength):
                        maxSubStringLength = right - left + 1
                        start = left
                        end = right
                left += 1
            right += 1
        return s[start: end + 1]
A = Solution()
print(A.longestPalindrome("cbbd"))

        