from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given n pairs of parentheses, write a function to generate
    all combinations of well-formed parentheses.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        pass
    
if __name__ == '__main__':
    sol = Solution()
    
    n = 3
    output = ["((()))","(()())","(())()","()(())","()()()"]
    assertEq(n, output, sol.generateParenthesis(n))

    n = 1
    output = ["()"]
    assertEq(n, output, sol.generateParenthesis(n))
 