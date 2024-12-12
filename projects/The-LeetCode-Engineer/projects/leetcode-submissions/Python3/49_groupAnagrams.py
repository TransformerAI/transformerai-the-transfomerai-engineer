from typing import List
from utils_code.test import assertEq
from collections import defaultdict

class Solution:
    """
    Given an array of strings strs, group the anagrams
    together. You can return the answer in any order.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # self.handleConstraints(strs)
        results = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ ord(c) - ord('a')] += 1
            results[tuple(count)].append(s)
        return results.values()
    
    
    
if __name__ == "__main__":
    sol = Solution()
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    assertEq(strs, output, sol.groupAnagrams(strs))

    strs = [""]
    output = [[""]]
    assertEq(strs, output, sol.groupAnagrams(strs))
    
    strs = ["a"]
    output = [["a"]]
    assertEq(strs, output, sol.groupAnagrams(strs))
 

