from dataStruct.single_link_list import *
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if k <= 1:
            return head
        lenth = 0
        item = head
        while item:
            lenth += 1
            item = item.next

        if k > lenth:
            return head
        yushu = lenth//k
        dummyHead = Node(0)
        dummyHead.next = head
        count = 1
        pre = dummyHead
        cur = dummyHead.next
        tail = None
        while cur and cur.next and yushu > 0:
            if count < k:
                if count == k-1:
                    tail = cur.next.next

                count += 1
            else:
                front = pre.next
                pre.next.next = tail
                pre.next = cur
                cur = cur.next
                count = 1
                pre = front
                yushu -= 1
        return dummyHead.next

if __name__ == "__main__":
    link = [1,2,3]
    singlelist = singleList()
    for i in link:
        singlelist.append(i)

    sol = Solution()
    a = sol.reverseKGroup(singlelist.head,3)
    print(a)
    while a:
        print(a.data)
        a = a.next