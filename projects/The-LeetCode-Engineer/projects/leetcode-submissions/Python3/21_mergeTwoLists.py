from typing import List, Optional

from utils_code.test import assertEq

class ListNode:
    def __init__(self, val: int =0, next: 'ListNode' =None):
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
    You are given the heads of two sorted linked lists list1 
    and list2.

    Merge the two lists into one sorted list. The list should 
    be made by splicing together the nodes of the first two lists.

    Return the head of the merged linked list.
    """
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
             
        return dummy.next
    
if __name__ == '__main__':
    sol = Solution()
    
    list1 = listToListNode([1,2,4])
    list2 = listToListNode([1,3,4])
    output = listToListNode([1,1,2,3,4,4])
    assertEq(listNodeToList(list1), listNodeToList(output), listNodeToList(sol.mergeTwoLists(list1, list2)))

    list1 = listToListNode([])
    list2 = listToListNode([])
    output = listToListNode([])
    assertEq(listNodeToList(list1), listNodeToList(output), listNodeToList(sol.mergeTwoLists(list1, list2)))
    
    list1 = listToListNode([])
    list2 = listToListNode([0])
    output = listToListNode([0])
    assertEq(listNodeToList(list1), listNodeToList(output), listNodeToList(sol.mergeTwoLists(list1, list2)))