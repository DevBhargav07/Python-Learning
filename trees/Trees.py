# learning trees using python
from __future__ import annotations
from dataclasses import dataclass
from collections import deque

@dataclass
class TreeNode:
    val: int
    left: TreeNode | None = None
    right: TreeNode | None = None

    def __str__(self):
        return str(self.val)


A = TreeNode(1)
B = TreeNode(2)
C = TreeNode(3)
D = TreeNode(4)

E = TreeNode(5)
F = TreeNode(6)
G = TreeNode(7)

A.left = B
A.right = C
B.left = E
C.left = F
B.right = D
C.right = G

'''
      1 
  2       3 

5   4   6    7

'''

# now we have to write the tree traversals
def pre_order_traversal(node):
    if not node:
        return
    print(node, end=",")
    pre_order_traversal(node.left)
    pre_order_traversal(node.right)

def in_order_traversal(node):
    if not node:
        return
    in_order_traversal(node.left)
    print(node, end=",")
    in_order_traversal(node.right)

def post_order_traversal(node):
    if not node:
        return
    post_order_traversal(node.left)
    post_order_traversal(node.right)
    print(node, end=",")

# Printing the trees node using conecpt of BFS
def level_order(node):
    q = deque()
    q.append(node)

    while q:
        node = q.popleft()
        print(node, end=",")
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

def height(node):
    # using recursion
    # if node is None:
    #     return 0
    # return 1 + max(height(node.left), height(node.right))

    # using iterative bfs
    if not node:
        return 
    level = 0
    q = deque([node])

    while q:
        for _ in range(len(q)):
            crnt = q.popleft()
            if crnt.left:
                q.append(crnt.left)
            if crnt.right:
                q.append(crnt.right)
        level += 1
    return level
    

def Search(node, target):
    if not node:
        return False # not found
    if node.val == target:
        return True
    return Search(node.left, target) or Search(node.right, target)


print(pre_order_traversal(A))
print(in_order_traversal(A))
print(post_order_traversal(A))

level_order(A)
print(f'\nSearching -1 in tree : {Search(A, -1)}')
print(f'\nLevel ordering: {level_order(A)}')
print(f'\n Height of Tree: {height(A)}')
