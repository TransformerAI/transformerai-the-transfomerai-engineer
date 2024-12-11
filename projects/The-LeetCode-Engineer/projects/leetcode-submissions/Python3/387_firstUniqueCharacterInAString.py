from typing import List

from utils_code.test import assertEq


class Solution:
    """
    Given a string s, find the first non-repeating character in it
    and return its index. If it does not exist, return -1.
    """
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in range(len(s)):
            d[s[i]] = []
        for i in range(len(s)):
            d[s[i]].append(i)
        
        for a, v in d.items():
            if len(v) == 1:
                return v[0]
        return -1
 
if __name__ == "__main__":
    sol = Solution()
    
    s = "leetcode"
    output = 0
    assertEq(s, output, sol.firstUniqChar(s))
    
    s = "loveleetcode"
    output = 2
    assertEq(s, output, sol.firstUniqChar(s))

    s = "aabb"
    output = -1
    assertEq(s, output, sol.firstUniqChar(s))

 