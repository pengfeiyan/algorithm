'''leetcode 19  双指针移动'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        pre,quit = dummyHead,dummyHead
        for i in range(0,n+1):
            quit = quit.next
        while quit:
            pre = pre.next
            quit = quit.next
        delNode = pre.next
        pre.next = delNode.next
        del delNode
        return dummyHead.next