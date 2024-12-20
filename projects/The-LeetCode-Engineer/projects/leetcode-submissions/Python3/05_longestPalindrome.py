from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given a string s, return the longest palindromic substring in s.
    """
    def longestPalindrome(self, s: str) -> str:
        res = ''
        resLen = 0
        
        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
        
if __name__ == '__main__':
    sol = Solution()

    s = "babad"
    output = "bab"
    assertEq(s, output, sol.longestPalindrome(s))
    
    s = "cbbd"
    output = "bb"
    assertEq(s, output, sol.longestPalindrome(s))
