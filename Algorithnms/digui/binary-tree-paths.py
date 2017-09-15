# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        ret = []
        if not root:
            return ret
        if not root.left and not root.right:
            ret.append(str(root.val))
        for i in self.binaryTreePaths(root.left):
            s1 = str(root.val)+'->'+i
            ret.append(s1)
        for j in self.binaryTreePaths(root.right):
            s1 = str(root.val)+'->'+j
            ret.append(s1)
        return ret