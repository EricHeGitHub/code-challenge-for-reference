class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def printTree(self):
        treeHeight = Node.getHeight(self)
        self._printTree(self, 0)

    def _printTree(self,node, indent):
        if node.left is not None:
            self._printTree(node.left, indent + 1)
        nodeHeight = Node.getHeight(node)
        print(indent * "\t" +str(node.data))
        if node.right is not None:
            self._printTree(node.right, indent + 1)



    def insert(self, data):
        if not self.data:
            self.data = data
        else:
            if self.data > data:
                if self.right == None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            if self.data < data:
                if self.left == None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
    def delete(self, val):
        #To be implemented
        pass
    def getHeight(n):
        if n.left == None and n.right == None:
            return 1
        leftHeight = 0
        leftHeight = 0
        if n.left:
            leftHeight = Node.getHeight(n.left)
        if n.right:
            rightHeight = Node.getHeight(n.right)
        return 1 + max(leftHeight, rightHeight)


if __name__ == "__main__":
    root = Node(12)
    root.insert(6)
    root.insert(14)
    root.insert(3)
    root.insert(7)
    root.insert(19)
    root.insert(1)
    root.insert(5)
    root.insert(4)
    root.insert(13)
    root.printTree()
