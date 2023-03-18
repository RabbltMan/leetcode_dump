class Solution:
    def isPalindrome(self, subString):
        for i in range(len(subString)):
            if (subString[i] != subString[-i - 1]):
                return False
        return True

    def singleCheck(self, a: str, b: str) -> bool:
        aPointer, bPointer = 0, len(b) - 1
        while (aPointer < bPointer and a[aPointer] == b[bPointer]):
            aPointer += 1
            bPointer -= 1
        return self.isPalindrome(b[aPointer: bPointer + 1]) or self.isPalindrome(a[aPointer: bPointer + 1])

    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        return self.singleCheck(a, b) or self.singleCheck(b, a)