# https://leetcode.com/problems/add-two-numbers/
# You are given two linked lists representing two non-negative numbers.
# The digits are stored in reverse order and
# each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.

# Iterate over lists. Add to result a node with
# the the sum of input nodes plus carry, mod 10.
# Time - O(max(m,n)) where m and n are input list lengths.
# Space - O(max(m,n)), output will be at most one digit more than longest input.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        q = 0
        while l1 and l2:
            value = l1.val + l2.val + q
            q, r = divmod(value, 10)
            curr.next = ListNode(r)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next

        while l1:
            value = l1.val + q
            q, r = divmod(value, 10)
            curr.next = ListNode(r)
            curr = curr.next
            l1 = l1.next

        while l2:
            value = l2.val + q
            q, r = divmod(value, 10)
            curr.next = ListNode(r)
            curr = curr.next
            l2 = l2.next

        if q > 0:
            curr.next = ListNode(q)
        return dummy.next
