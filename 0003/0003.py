class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = 0
        leftCursor = 0
        for rightCursor in range(2, len(s) + 1):
            subString = s[leftCursor: rightCursor]
            if subString[-1] in subString[0: -1]:
                if len(subString) - 1 > maxLength:
                    maxLength = len(subString) - 1
                dupChar = subString[-1]
                leftCursor += subString.find(dupChar) + 1
                subString = s[leftCursor: rightCursor]
        finalLen = len(s) - leftCursor
        if finalLen > maxLength:
            return finalLen
        return maxLength

# A = Solution()
# print(A.lengthOfLongestSubstring("abcb"))