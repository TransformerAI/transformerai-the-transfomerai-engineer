from typing import List

from utils_code.test import assertEq

class Solution:
    """
    Given a string s, find the length of the longest substring 
    without repeating characters.
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


if __name__ == "__main__":
    sol = Solution()
    
    s = "abcabcbb"
    output = 3
    assertEq(s, output, sol.lengthOfLongestSubstring(s))
    
    s = "bbbbb"
    output = 1
    assertEq(s, output, sol.lengthOfLongestSubstring(s))

    s = "pwwkew"
    output = 3
    assertEq(s, output, sol.lengthOfLongestSubstring(s))
