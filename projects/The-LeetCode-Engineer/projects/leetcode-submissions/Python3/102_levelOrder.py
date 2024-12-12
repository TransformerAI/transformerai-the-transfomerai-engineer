from typing import List, Optional

from utils_code.test import assertEq


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    """
    Given the root of a binary tree, return the level order 
    traversal of its nodes' values. (i.e., from left to right, level by level).
    """
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        pass
    
if __name__ == '__main__':
    sol = Solution()
    
    root = [3,9,20,None,None,15,7]
    output = [[3],[9,20],[15,7]]
    assertEq(root, output, sol.levelOrder(root))

    root = [1]
    output = [[1]]
    assertEq(root, output, sol.levelOrder(root))
    
    root = []
    output = []
    assertEq(root, output, sol.levelOrder(root))
    