'''leetcode 206'''
from dataStruct.single_link_list import *

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        elif m > n:
            maxs,mins = m,n
        else:
            maxs,mins = n,m






l = singleList()
arr = [1,2,3,4,5]
for i in arr:
    l.append(i)


