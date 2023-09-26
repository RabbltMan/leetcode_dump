class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % (2 * n - 2)
        return time + 1 if time < n else n - time + n - 1