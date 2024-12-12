from typing import List, Optional

from utils_code.test import assertEq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    """
    You are given the heads of two sorted linked lists list1 
    and list2.

    Merge the two lists into one sorted list. The list should 
    be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pass
    
if __name__ == '__main__':
    sol = Solution()
    
    list1 = [1,2,4]
    list2 = [1,3,4]
    output = [1,1,2,3,4,4]
    assertEq(list1, output, sol.mergeTwoLists(list1, list2))

    list1 = []
    list2 = []
    output = []
    assertEq(list1, output, sol.mergeTwoLists(list1, list2))
    
    list1 = []
    list2 = [0]
    output = [0]
    assertEq(list1, output, sol.mergeTwoLists(list1, list2))