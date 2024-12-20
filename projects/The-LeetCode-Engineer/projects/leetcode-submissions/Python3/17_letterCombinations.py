from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given a string containing digits from 2-9 inclusive, return 
    all possible letter combinations that the number could represent. 
    Return the answer in any order.

    A mapping of digits to letters (just like on the telephone buttons) 
    is given below. 
    
    Note that 1 does not map to any letters.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitsToChar = { 
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "qprs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        def backtrack(i, curStr):
            if len(curStr) == len(digits):
                res.append(curStr)
                return
            for c in digitsToChar[digits[i]]:
                backtrack(i + 1, curStr + c)
        if digits:
            backtrack(0, "")
        return res
    
if __name__ == '__main__':
    sol = Solution()
    
    digits = "23"
    output = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assertEq(digits, output, sol.letterCombinations(digits))

    digits = ""
    output = []
    assertEq(digits, output, sol.letterCombinations(digits))

    digits = "2"
    output = ["a","b","c"]
    assertEq(digits, output, sol.letterCombinations(digits))