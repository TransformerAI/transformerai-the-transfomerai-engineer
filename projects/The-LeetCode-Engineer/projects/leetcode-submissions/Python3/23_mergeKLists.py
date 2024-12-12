from typing import List, Optional

from utils_code.test import assertEq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def listNodeToList(node: ListNode) -> list:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def listToListNode(lsst: list):
    if lsst == None or len(lsst) == 0:
        return None
    dummy = ListNode()
    current = dummy
    for val in lsst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

class Solution():
    """
    You are given an array of k linked-lists lists, each 
    linked-list is sorted in ascending order.

    Merge all the linked-lists into one sorted linked-list 
    and return it.
    """
    def mergeKLists(self, lists: list) -> ListNode:
        if not lists or len(lists) == 0:
            return None
        
        while len(lists) > 1:
            mergedLists = []
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))
            lists = mergedLists
        return lists[0]
    
    def mergeList(self, l1, l2):
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2: 
            tail.next = l2
        return dummy.next
    
if __name__ == '__main__':
    sol = Solution()
    
    lists = [listToListNode([1,4,5]),listToListNode([1,3,4]),listToListNode([2,6])]
    output = [1,1,2,3,4,4,5,6]
    assertEq(lists, output, listNodeToList(sol.mergeKLists(lists)))

    lists = []
    output = []
    assertEq(lists, output, listNodeToList(sol.mergeKLists(lists)))

    # lists = listToListNode([[]])
    # output = listToListNode([])
    # assertEq(listNodeToList(lists), listNodeToList(output), listNodeToList(sol.mergeKLists(lists)))
