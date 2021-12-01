class Node:
    def __init__(self, data, height, parent):
        self.left = -1
        self.right = -1
        self.parent = parent
        self.height = height
        self.data = data

def buildTree(currNode, currNum, h):
    # Fill Right
    if currNode.height < h:
        # Fill Right & call recursive
        currNode.right = Node(currNum, currNode.height+1, currNode)
        currNum-=1
        currNum = buildTree(currNode.right, currNum, h)

        # Fill Left & call recursive
        currNode.left = Node(currNum, currNode.height+1, currNode)
        currNum-=1
        currNum = buildTree(currNode.left, currNum, h)

    return currNum

def postOrder(node, q, sols):
    for i in range(len(q)):
        if q[i] == node.data:
            if node.parent != -1:
                sols[i] = node.parent.data
            else:
                sols[i] = -1
    if node.left != -1:
        sols = postOrder(node.left, q, sols)
        sols = postOrder(node.right, q, sols)
    return sols

def solution(h, q):
    currNum = 2 ** h - 1
    root = Node(currNum, 1, -1)
    buildTree(root, currNum-1, h)
    return postOrder(root, q, q)
