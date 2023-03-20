public class Solution {
    public string LongestPalindrome(string s) {
        int StringLength = s.Length;
        if (StringLength == 1) {
            return s;
        }
        int start = 0;
        int maxSubStringLength = 1;
        bool[,] state = new bool[StringLength, StringLength];

        for (int right = 1; right < StringLength; right++) {
            for (int left = 0; left < right; left ++) {
                if (s[left] == s[right] && (right - left <= 2 || state[left, right])) {
                    state[left - 1, right + 1] = true;
                }
                if (right - left + 1 > maxSubStringLength) {
                    maxSubStringLength = right - left + 1;
                    start = left;
                }
            }
        }
        return s.Substring(start, maxSubStringLength);
    }
}

class A {
    public static void Main() {
        Solution sol = new Solution();
        Console.WriteLine(sol.LongestPalindrome("aaaa"));
    }
}