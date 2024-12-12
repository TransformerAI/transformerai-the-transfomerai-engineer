from typing import List, Optional

from utils_code.test import assertEq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    """
    Given the head of a linked list, reverse the nodes of the 
    list k at a time, and return the modified list.

    k is a positive integer and is less than or equal to the 
    length of the linked list. If the number of nodes is not 
    a multiple of k then left-out nodes, in the end, should 
    remain as it is.

    You may not alter the values in the list's nodes, only 
    nodes themselves may be changed.
    """
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        pass
    
if __name__ == '__main__':
    sol = Solution()
    
    head = [1,2,3,4,5]
    k = 2
    output = [2,1,4,3,5]
    assertEq(head, output, sol.reverseKGroup(head, k))

    head = [1,2,3,4,5]
    k = 3
    output = [3,2,1,4,5]
    assertEq(head, output, sol.reverseKGroup(head, k))