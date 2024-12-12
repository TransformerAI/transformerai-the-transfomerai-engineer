from typing import List, Optional

from utils_code.test import assertEq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution():
    """
    You are given an array of k linked-lists lists, each 
    linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list 
    and return it.
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pass
    
if __name__ == '__main__':
    sol = Solution()
    
    lists = [[1,4,5],[1,3,4],[2,6]]
    output = [1,1,2,3,4,4,5,6]
    assertEq(lists, output, sol.mergeKLists(lists))

    lists = []
    output = []
    assertEq(lists, output, sol.mergeKLists(lists))

    lists = [[]]
    output = []
    assertEq(lists, output, sol.mergeKLists(lists))
