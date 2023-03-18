class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def singleCheck(a: str, b: str) -> bool:
            aPointer, bPointer = 0, len(b) - 1
            while (a[aPointer] == b[bPointer] and aPointer < bPointer):
                aPointer += 1
                bPointer -= 1
            return b[aPointer: bPointer + 1] == b[aPointer: bPointer + 1][::-1] or a[aPointer: bPointer + 1] == a[aPointer: bPointer + 1][::-1]
        return singleCheck(a, b) or singleCheck(b, a)