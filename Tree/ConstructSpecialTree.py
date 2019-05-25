'''
Given an array ‘pre[]’ that represents Preorder traversal of
a spacial binary tree where every node has either 0 or 2 children.
One more array ‘preLN[]’ is given which has only two possible values
‘L’ and ‘N’. The value ‘L’ in ‘preLN[]’ indicates that
the corresponding node in Binary Tree is a leaf node and
value ‘N’ indicates that the corresponding node is non-leaf node.
Write a function to construct the tree from the given two arrays.
'''

class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

    def printTree(self):
        level = 0
        self._printTree(level)

    def _printTree(self, level):
        if self.left:
            self.left._printTree(level + 1)
        print("\t" * level + str(self.data))
        if self.right:
            self.right._printTree(level + 1)

    def getHeight(self):
        if self == None:
            return 0
        leftHeight = 0
        rightHeight = 0
        if self.left:
            leftHeight = self.left.getHeight()
        if self.right:
            rightHeight = self.right.getHeight()
        return 1 + max(leftHeight, rightHeight)

def ConstructSpecialTree(node, pre, preLN):
    node.data = pre[0]
    if preLN[0] == "L":
        return pre, preLN
    elif preLN[0] == "N":
        if len(pre) > 1 and len(preLN) > 1:
            node.left = Node()
            pre, preLN = ConstructSpecialTree(node.left, pre[1:], preLN[1:])
        if len(pre) > 1 and len(preLN) > 1:
            node.right = Node()
            pre, preLN = ConstructSpecialTree(node.right, pre[1:], preLN[1:])
        return pre, preLN


pre = [10, 30, 20, 5, 15]
preLN = ['N', 'N', 'L', 'L', 'L']

root = Node()
ConstructSpecialTree(root, pre, preLN)
root.printTree()
