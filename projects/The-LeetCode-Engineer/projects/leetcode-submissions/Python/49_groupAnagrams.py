from typing import List
from collections import defaultdict

from utils_code.configuration import Configuration
from utils_code.constraints.predicate import predicate

class Solution:
    def handleConstraints(self, strs: List[str]):
        predicate(lambda: 1 <= len(strs) <= 104, None, f"String-Collection length is incorrect: {len(strs)}")        
        for str in strs:
            predicate(lambda: 0 <= len(str) <= 100, None, f"String length is incorrect: {len(str)}")
            predicate(lambda: str.lower() == str, None, f"strs[i] {str} consists of lowercase English letters.")

    
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
 

