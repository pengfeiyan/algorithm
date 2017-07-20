# coding=utf-8
import random,time

class Node:
   def __init__(self,data):
       self.data = data
       self.left = None
       self.right = None
class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def insert(self,data):
        item = Node(data)
        if not self.root:
            self.root = item
        node = self.root
        while node:
            if node.data > data:
                if node.left == None:
                    node.left = item
                    return
                node = node.left
            elif node.data < data:
                if node.right == None:
                    node.right = item
                    return
                node = node.right
            else:
                node.data = data
                return

    def search(self,target):
        node = self.root
        while node:
            if node.data == target:
                return True
            elif node.data < target:
                node = node.right
            else:
                node = node.left
        return False


    def preOrder(self,root):
        if root == None:
            return
        print(root.data)
        self.preOrder(root.left)
        self.preOrder(root.right)

    def inOrder(self,root):
        if root == None:
            return
        self.inOrder(root.left)
        print(root.data)
        self.inOrder(root.right)

    '''内存回收，会使用后序遍历，将孩子节点删除，才能安全的删除父亲节点'''
    def postOrder(self,root):
        if root == None:
            return
        self.postOrder(root.left)
        self.postOrder(root.right)
        print(root.data)

    def levelOrder(self,root):
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)




arr = [5,1,4,7,3,6,9,2,8]
bst=BST()
for i in arr:
    bst.insert(i)

bst.levelOrder(bst.root)



