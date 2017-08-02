'''leetcode 24 虚拟头节点'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead
        while pre.next and pre.next.next:
            node1 = pre.next
            node2 = pre.next.next
            next = node2.next

            node2.next = node1
            node1.next = next
            pre.next = node2
            pre = node1

        retNode = dummyHead.next
        del dummyHead
        return retNode
