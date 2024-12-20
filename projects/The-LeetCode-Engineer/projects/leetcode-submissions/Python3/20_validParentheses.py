from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given a string s containing just the characters 
    '(', ')', '{', '}', '[' and ']', 
    determine if the input string is valid.

    An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.
    """
    def isValid(self, s: str) -> bool:
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
    assertEq(s, output, sol.isValid(s))

    s = "()[]{}"
    output = True
    assertEq(s, output, sol.isValid(s))
    
    s = "(]"
    output = False
    assertEq(s, output, sol.isValid(s))
    
    s = "([])"
    output = True
    assertEq(s, output, sol.isValid(s))
 