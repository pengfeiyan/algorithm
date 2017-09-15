from dataStruct.tree_and_bianli import *
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not q and not p:
            return True
        elif not p or not q:
            return False
        elif p.elem != q.elem:
            return False
        elif p.elem == q.elem:
            return self.isSameTree(p.lchild,q.lchild) and self.isSameTree(p.rchild,q.rchild)
t1 = [10,5,15]
t2 = [10,5,15]
tree1 = Tree()
tree2 = Tree()
for i in t1:
    tree1.add_node(i)
for j in t2:
    tree2.add_node(j)

sol = Solution()
print(sol.isSameTree(tree1.root,tree2.root))