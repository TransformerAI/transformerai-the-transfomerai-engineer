
from utils_code.constraints.predicate import predicate

class Solution:
    def handleConstraints(self, s, t):
        m = len(s)
        n = len(t)
        predicate(lambda: 1 <= m and n <= 105, None, "1 <= m and n <= 105")
        predicate(lambda: 
            any(c.isupper() for c in s) and 
            any(c.islower() for c in s) and 
            any(c.isupper() for c in t) and
            any(c.islower() for c in t), None, "s and t must consist of uppercase and lowercase English letters.") 
    
    def minWindow(self, s: str, t: str) -> str:        
        if t == "": return ""
        countT, window = {}, {}
        for c in t:
            countT[c] = 1 + countT.get(c, 0)
            
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l: r+1] if resLen != float("infinity") else ""
    

sol = Solution()
s = "ADOBECODEBANC"
t = "ABC"
min = sol.minWindow(s, t)
output = "BANC"
print(min)
print(output)
print(min == output)


s = "a"
t = "a"
min = sol.minWindow(s, t)
output = "a"
print(min)
print(output)
print(min == output)

s = "a"
t = "aa"
min = sol.minWindow(s, t)
output = ""
print(min)
print(output)
print(min == output) 