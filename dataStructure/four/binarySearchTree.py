# coding=utf-8
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
            if node.data < data:
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




    def visit(self,root):
        if root == None:
            return
        print(root.data)
        self.visit(root.left)
        self.visit(root.right)


arr = [5,1,4,7,3,6,9,2,8]
bst=BST()
for i in arr:
    bst.insert(i)
print(bst.search())