from typing import List, Optional

from utils_code.test import assertEq
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution():
    """
    Given the root of a binary tree, return the zigzag level order 
    traversal of its nodes' values. (i.e., from left to right, then 
    right to left for the next level and alternate between).
    """
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        q = deque([root] if root else [])    
        while q:
            level = []
            for i in range(len(q)):
                n = q.popleft()
                level.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            level = list(reversed(level)) if len(res) % 2 else level
            res.append(level)
        return res
            
if __name__ == '__main__':
    sol = Solution()
    
    root = [3,9,20,None,None,15,7]
    output = [[3],[20,9],[15,7]]
    assertEq(root, output, sol.zigzagLevelOrder(root))

    root = [1]
    output = [[1]]
    assertEq(root, output, sol.zigzagLevelOrder(root))
    
    root = []
    output = []
    assertEq(root, output, sol.zigzagLevelOrder(root))