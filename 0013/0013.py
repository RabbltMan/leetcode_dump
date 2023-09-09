class Solution:
    def romanToInt(self, s: str) -> int:
        table = {'IV': -2, "IX": -2, "XL": -20, "XC": -20, "CD": -200, "CM": -200, 'I': 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, 'M': 1000}
        res = 0
        for key, value in table.items():
            res += s.count(key) * value

        return res
    