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
        stack = []
        close_to_open = {
            ")": "(", 
            "]" : "[", 
            "}" : "{"
        }
        for c in s:
            if c in close_to_open:
                if stack and stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
    
    
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
    