from typing import List

from utils_code.test import assertEq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    """
    """
    def maxPathSum(self, root: TreeNode) -> int:
        res = [root.val]
        def dfs(node: TreeNode):
            if not node:
                return 0
            left_max = dfs(node.left)
            right_max = dfs(node.right)
            left_max = max(left_max, 0)
            right_max = max(right_max, 0)
            
            res[0] = max(res[0], node.val + left_max + right_max)
            
            return node.val + max(left_max, right_max)
        dfs(root)
        return res[0]
    
if __name__ == '__main__':
    sol = Solution()