from typing import List, Optional

from utils_code.test import assertEq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    """
    Given the root of a binary tree, return its maximum depth.

    A binary tree's maximum depth is the number of nodes along 
    the longest path from the root node down to the farthest 
    leaf node.
    """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return res
            
if __name__ == '__main__':
    sol = Solution()
    
    root = [3,9,20,None,None,15,7]
    output = 3
    assertEq(root, output, sol.maxDepth(root))

    root = [1,None,2]
    output = 2
    assertEq(root, output, sol.maxDepth(root))