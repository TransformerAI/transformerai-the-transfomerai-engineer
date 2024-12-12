from typing import List
from collections import defaultdict
from utils_code.test import assertEq


class Solution:
    """
    Given a string s, find the first non-repeating character in it
    and return its index. If it does not exist, return -1.
    """
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
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

 