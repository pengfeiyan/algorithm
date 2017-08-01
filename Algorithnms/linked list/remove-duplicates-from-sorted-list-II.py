'''leetcode  82'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from dataStruct.single_link_list import *
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = Node('a')
        dummyHead.next = head
        pre = dummyHead
        cur = dummyHead.next
        flag = 0
        while cur.next:
            if cur.data == cur.next.data:
                flag = 1
                delNode = cur.next
                cur.next = delNode.next
                del delNode
            else:
                if flag:
                    pre.next = cur.next
                    delNode = cur
                    cur = cur.next
                    del delNode
                    flag = 0
                else:
                    pre = cur
                    cur = cur.next
        return dummyHead.next

if __name__ == "__main__":
    linklist = singleList()
    arr = [1,1,2,3]
    for i in arr:
        linklist.append(i)
    # linklist.show()
    sol = Solution()
    sol.deleteDuplicates(linklist.head)
    linklist.show()
