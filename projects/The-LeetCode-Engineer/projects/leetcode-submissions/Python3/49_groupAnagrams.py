from typing import List
from utils_code.test import assertEq
from collections import defaultdict

class Solution:
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
    s = Solution()
    
    strs = ["eat","tea","tan","ate","nat","bat"]
    output = [["bat"],["nat","tan"],["ate","eat","tea"]]
    out = s.groupAnagrams(strs)
    print(strs)
    print(out)
    print(output == out)

    strs = [""]
    output = [[""]]
    out = s.groupAnagrams(strs)
    print(strs)
    print(out)
    print(output == out)
    
    strs = ["a"]
    output = [["a"]]
    out = s.groupAnagrams(strs)
    print(strs)
    print(out)
    print(output == out)
 

