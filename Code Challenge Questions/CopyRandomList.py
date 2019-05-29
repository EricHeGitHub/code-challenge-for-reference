'''
A linked list is given such that
each node contains an additional random pointer
which could point to any node in the list or null.

Input:
{"$id":"1","next":{"$id":"2","next":null,"random":{"$ref":"2"},"val":2},
"random":{"$ref":"2"},"val":1}

Explanation:
Node 1's value is 1, both of its next and random pointer points to Node 2.
Node 2's value is 2, its next pointer points to null
and its random pointer points to itself.

# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
'''

def copyRandomList(self, head):
    if head is None:
        return None
    if head.next is None:
        newHead = Node(head.val, None, None)
        if head.random is not None:
            newHead.random = newHead
        return newHead

    restoreOriginalNext = []
    copiedHead = Node(head.val, None, None)
    node = head.next # node is the next node to be copied
    head.next = copiedHead
    copiedHead.random = head

    restoreOriginalNext.append(node)

    while node is not None:
        copiedHead.next = Node(node.val, None, None)
        nextNode = node.next
        node.next = copiedHead.next
        copiedHead.next.random = node
        node = nextNode
        copiedHead = copiedHead.next
        restoreOriginalNext.append(nextNode)

    node = head
    copiedHead = head.next

    while node is not None:
        if node.random is not None:
            node.next.random = node.random.next # set random in new list
        else:
            node.next.random  = None  # deal with scenarios when random is None
        if node.next.next:
            node = node.next.next.random
        else:
            node = None

    node = head
    while node is not None:
        node.next = restoreOriginalNext[0]
        restoreOriginalNext = restoreOriginalNext[1:] #restore old linked list
        node = node.next

    return copiedHead
