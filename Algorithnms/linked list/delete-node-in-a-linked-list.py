'''leetcode 237'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''这个题只给了需要删除的节点，但是没有该节点的pre，不可能删除此节点的，所以需要改变此节点的值为next的值，然后删除next'''
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if not node:
            return
        else:
            node.val = node.next.val
            delNode = node.next
            node.next = delNode.next
            del delNode
            return
