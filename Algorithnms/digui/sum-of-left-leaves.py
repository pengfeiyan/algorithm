from dataStruct.tree_and_bianli import *
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)


t = [3,9,20,None,None,15,7]
tree = Tree()
for i in t:
    tree.add_node(i)

sol = Solution()
print(sol.sumOfLeftLeaves(tree.root))