class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                  'C': 100, 'D': 500, 'M': 1000 }
        res = 0
        length = len(s)
        for i in range(length):
            si = roman[s[i]]
            sip = roman[s[i + 1]] if i + 1 < length else 0
            if i + 1 < length and si < sip:
                res -= si
            else:
                res += si
        return res