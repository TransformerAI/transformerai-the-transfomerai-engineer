from typing import List

from utils_code.test import assertEq


 
class Solution:
    """    
    Given a string s containing only three types of characters: 
    '(', ')' and '*', return true if s is valid.

    The following rules define a valid string:

    Any left parenthesis '(' must have a corresponding right parenthesis ')'.
    Any right parenthesis ')' must have a corresponding left parenthesis '('.
    Left parenthesis '(' must go before the corresponding right parenthesis ')'.
    
    '*' could be treated as a single right parenthesis ')' or a single left 
    parenthesis '(' or an empty string "".
    """
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0
        for c in s:
            if c == "(":
                leftMin += 1
                leftMax += 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin -1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0
    
    
    
if __name__ == "__main__":
    sol = Solution()

    s = "()"
    output = True
    assertEq(s, output, sol.checkValidString(s))
    
    s = "(*)"
    output = True
    assertEq(s, output, sol.checkValidString(s))
    
    s = "(*))"
    output = True
    assertEq(s, output, sol.checkValidString(s))
    