from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given n pairs of parentheses, write a function to generate
    all combinations of well-formed parentheses.
    """
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        
        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()
        backtrack(0, 0)
        return res
    
if __name__ == '__main__':
    sol = Solution()
    
    n = 3
    output = ["((()))","(()())","(())()","()(())","()()()"]
    assertEq(n, output, sol.generateParenthesis(n))

    n = 1
    output = ["()"]
    assertEq(n, output, sol.generateParenthesis(n))
 