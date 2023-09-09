class Solution:
    def intToRoman(self, num: int) -> str:
        RomanTable = [['', 'M', 'MM', 'MMM'],
                      ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
                      ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
                      ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']]
        return RomanTable[0][num//1000] + RomanTable[1][num % 1000 // 100] + RomanTable[2][num % 100 // 10] + RomanTable[3][num % 10]