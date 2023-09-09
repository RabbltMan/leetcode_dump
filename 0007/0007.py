class Solution:
    def reverse(self, x: int) -> int:
        if (x < 0):
            x = '-' + str(-x)[::-1]
        else:
            x = str(x)[::-1]
        x = int(x)
        
        return x if -2147483648 < x < 2147483647 else 0