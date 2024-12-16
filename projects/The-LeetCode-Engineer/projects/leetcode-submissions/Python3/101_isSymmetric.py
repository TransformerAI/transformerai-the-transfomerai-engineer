from typing import List

from utils_code.test import assertEq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution():
    """
    Given the root of a binary tree, check whether it is a mirror 
    of itself (i.e., symmetric around its center).
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        def dfs(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            
            return (
                left.val == right.val and 
                dfs(left.left, right.right) and 
                dfs(left.right, right.left)
            )
        dfs(root.left, root.right)
        
if __name__ == '__main__':
    sol = Solution()