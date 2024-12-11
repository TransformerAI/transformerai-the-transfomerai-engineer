
from utils_code.test import assertEq

# Definition for singly-linked list.
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
    You are given two non-empty linked lists representing two 
    non-negative integers. The digits are stored in reverse order, 
    and each of their nodes contains a single digit. Add the two 
    numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading 
    zero, except the number 0 itself.
    """
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode()
        current = dummy
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            current.next = ListNode(val)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next        
    
if __name__ == '__main__':
    sol = Solution()

    l1 = listToListNode([2, 4, 3])
    l2 = listToListNode([5, 6, 4])
    output = [7, 0, 8]
    assertEq(l1, output, listNodeToList(sol.addTwoNumbers(l1, l2)))

    l1 = ListNode(0)
    l2 = ListNode(0)
    output = [0]
    assertEq(l1, output, listNodeToList(sol.addTwoNumbers(l1, l2)))
    
    l1 = listToListNode([9,9,9,9,9,9,9])
    l2 = listToListNode([9,9,9,9])
    output = [8,9,9,9,0,0,0,1]
    assertEq(l1, output, listNodeToList(sol.addTwoNumbers(l1, l2)))