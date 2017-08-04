'''leetcode 234'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''没有想出O（1）空间复杂度的'''
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ans = []
        if not head or not head.next:
            return True
        else:
            while head:
                ans.append(head.val)
                head = head.next
        i,j = 0,len(ans)-1
        while i < j:
            if ans[i] == ans[j]:
                i += 1
                j -= 1
            else:
                return False
        return True
