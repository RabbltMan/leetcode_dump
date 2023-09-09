from typing import *

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        for i in range(len(strs[0])):
            prefix1 = strs[0][: i+1]
            for word in strs:
                if not word.startswith(prefix1):
                    return prefix
            prefix = prefix1

        return prefix
    