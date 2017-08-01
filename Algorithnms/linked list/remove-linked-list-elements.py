'''leetcode 203 链表虚拟头节点'''
from dataStruct.single_link_list import *

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # def removeElements(self, head, val):
    #     """
    #     :type head: ListNode
    #     :type val: int
    #     :rtype: ListNode
    #     """
    #     while head and head.val == val:
    #         delNode = head
    #         head = delNode.next
    #         del delNode
    #
    #     if not head:
    #         return head
    #
    #     cur = head
    #     while cur.next:
    #         if cur.next.val == val:
    #             delNode = cur.val
    #             cur.next = delNode.next
    #             del delNode
    #         else:
    #             cur = cur.next
    #     return head

    '''虚拟头节点'''
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummyHead = Node(0)
        dummyHead.next = head
        cur = dummyHead
        while cur.next:
            if cur.next.val == val:
                delNode = cur.next
                cur.next = delNode.next
                del delNode
            else:
                cur = cur.next
        retNode = dummyHead.next
        del dummyHead
        return retNode