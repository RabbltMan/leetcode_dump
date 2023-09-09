class Solution:
    def convert(self, s: str, numRows: int) -> str:
        seq = [row for row in range(numRows)]
        seq += seq[-2: 0: -1]
        rows = [''] * numRows
        
        for i, char in enumerate(s):
            rows[seq[i % len(seq)]] += char

        return ''.join(rows)