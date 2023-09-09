class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (not(x % 10) and x != 0):
            return False

        rev = 0
        while(rev < x):
            rev = rev * 10 + x % 10
            x //= 10
        
        return rev // 10 == x or rev == x