from typing import List, Optional

from utils_code.test import assertEq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    """
    'Construct Binary Tree from Pre-Order and In-Order Traversal'
    Given two integer arrays preorder and inorder where preorder
    is the preorder traversal of a binary tree and inorder is the 
    inorder traversal of the same tree, construct and return the 
    binary tree.
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pass
    
if __name__ == '__main__':
    sol = Solution()
    
    preorder = [3,9,20,15,7]
    inorder = [9,3,15,20,7]
    output = [3,9,20,None,None,15,7]
    assertEq(preorder, output, sol.fn(preorder, inorder))

    preorder = [-1]
    inorder = [-1]
    output = [-1]
    assertEq(preorder, output, sol.fn(preorder, inorder))
 