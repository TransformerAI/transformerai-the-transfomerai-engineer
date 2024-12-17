from typing import List
from utils_code.test import assertEq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    """
    Given an integer n, return all the structurally unique BST's 
    (binary search trees), which has exactly n nodes of unique 
    values from 1 to n. Return the answer in any order.
    """
    def generateTrees(self, n: int) -> List[TreeNode]:

        pass

    
                
if __name__ == "__main__":
    sol = Solution()
    
    n = 3
    output = [
        [1,None,2,None,3],
        [1,None,3,2],
        [2,1,3],
        [3,1,None,None,2],
        [3,2,None,1]
    ]


    n = 1
    output = [[1]]
 