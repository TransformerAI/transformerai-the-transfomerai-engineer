
 
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
        pass
    
    
    
if __name__ == "__main__":
    sol = Solution()
    s = "()"
    output = True
    out = sol.checkValidString(s)
    print(out)

    s = "(*)"
    output = True
    out = sol.checkValidString(s)
    print(out)

    s = "(*))"
    output = True
    out = sol.checkValidString(s)
    print(out)
