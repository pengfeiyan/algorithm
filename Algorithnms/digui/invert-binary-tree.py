
'''leetcode 226'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left,root.right = root.right,root.left
        return root
a,b = 0,0
for x in range(100,1000,100):
    a,b = b,x/(x+602)
    print(x,(b-a))

for x in range(100,1000,100):
    print(x,x/(x+602))