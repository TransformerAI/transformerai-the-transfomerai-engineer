from typing import List, Optional

from utils_code.test import assertEq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listNodeToList(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

def listToListNode(lst):
    dummy = ListNode()
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

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
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0, head)
        groupPrev = dummy
        while True:
            kth = self.getKth(groupPrev, k)
            if not kth:
                break
            groupNext = kth.next
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            tmp =  groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next
    
    def getKth(self, curr: ListNode, k: int) -> ListNode:
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

if __name__ == '__main__':
    sol = Solution()

    head = listToListNode([1,2,3,4,5])
    k = 2
    output = [2,1,4,3,5]
    out = sol.reverseKGroup(head, k)
    print(listNodeToList(head))
    # assertEq(listNodeToList(head), output, listNodeToList())

    # head = [1,2,3,4,5]
    # k = 3
    # output = [3,2,1,4,5]
    # assertEq(head, output, sol.reverseKGroup(head, k))