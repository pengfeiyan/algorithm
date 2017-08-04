'''leetcode 61 双指针  未完成'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        lenth,item = 0,head
        while item:
            lenth += 1
            item = item.next
        if k==0:
            return head
        dummyHead = ListNode(0)
        dummyHead.next = head
        if lenth <= k:
            pre = dummyHead
            cur = dummyHead.next
            while cur and cur.next:
                next = cur.next
                cur.next = pre
                pre = cur
                cur = next
            return pre
        pre,quit = dummyHead,dummyHead
        for i in range(0,k):
            quit = quit.next
        while quit.next:
            pre = pre.next
            quit = quit.next
        dummyHead.next = pre.next
        pre.next = None
        quit.next = head
        return dummyHead.next