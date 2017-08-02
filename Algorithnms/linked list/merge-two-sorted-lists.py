'''leetcode 21'''
from dataStruct.single_link_list import *

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        else:
            dummyHead = Node(0)
            dummyHead.next = l1
            pre = dummyHead
            cur = dummyHead.next
            insert = l2
            while insert:
                insertNode = Node(insert.data)
                while cur:
                    if insert.data < cur.data:
                        pre.next = insertNode
                        insertNode.next = cur
                        pre = insertNode
                        break
                    else:
                        pre = cur
                        cur = cur.next
                else:
                    pre.next = insertNode
                    pre = insertNode
                    cur = None
                insert = insert.next
            return dummyHead.next

l1 = [2]
l2 = [1]
list1,list2 = singleList(),singleList()
for i in l1:
    list1.append(i)
for j in l2:
    list2.append(j)

sol = Solution()
sol.mergeTwoLists(list1.head,list2.head)
