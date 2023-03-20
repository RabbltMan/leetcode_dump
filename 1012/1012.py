from math import *
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        numArray = list(map(int, str(n + 1)))
        res = 0
        permTable = [0, 0, 9, 261, 4725, 67509, 831429, 9287109, 97654149, 994388229]
        arrayLength = len(numArray)
        res += permTable[arrayLength - 1]

        remaining = n - 10**(arrayLength - 1)
        notDup = 0
        used = set()
        for digit, fig in enumerate(numArray):
            for num in range(digit == 0, fig):
                if num not in used:
                    notDup += perm(9 - digit, arrayLength - digit - 1)
            if fig in used:
                break
            used.add(fig)
        res += remaining - notDup + 1
        return res
