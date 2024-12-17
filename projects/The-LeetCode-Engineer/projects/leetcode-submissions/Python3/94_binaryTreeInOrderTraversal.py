
from typing import List
from utils_code.test import assertEq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import enum
class TraversalMethod(enum.IntEnum):
    RECURSIVE = 1,
    ITERATIVE = 2

class Solution():
    """
    Given the root of a binary tree, return the inorder traversal 
    of its nodes' values.
    """
    
    def __init__(self, traversal: TraversalMethod = None):
        self.traversal = traversal
        if self.traversal == None:
            self.traversal = TraversalMethod.RECURSIVE
    
    def inorderTraversalRecur(self, root: TreeNode) -> List[int]:
        res = []
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)
        inorder(root)
        return res
    
    def inorderTraversalIter(self, root: TreeNode) -> List[int]:
        res = []
        stack = []
        currentNode = root
        
        while currentNode or stack:
            while currentNode:
                stack.append(currentNode)
                currentNode = currentNode.left
            currentNode = stack.pop()
            res.append(currentNode.val)
            currentNode = currentNode.right
        return res
    
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if self.traversal == TraversalMethod.RECURSIVE:
            return self.inorderTraversalRecur(root)
        elif self.traversal == TraversalMethod.ITERATIVE:
            return self.inorderTraversalIter(root)
    
if __name__ == "__main__":
    sol = Solution(TraversalMethod.ITERATIVE)
    
    root = TreeNode(val=1,
                 left=None, 
                 right=TreeNode(val=2, 
                    left=TreeNode(val=3)))
    output = [1,3,2]
    assertEq(root, output, sol.inorderTraversal(root))

    # root = [1,2,3,4,5,None,8,None,None,6,7,9]
    # output = [4,2,6,5,7,1,3,9,8]
    # assertEq(root, output, sol.inorderTraversal(root))

