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
# print(f'\nLevel ordering: {level_order(A)}')


# is ugly number
def is_ugly(num):
    if num <= 0:
        return False
    if num == 1:
        return True
    while(num % 2 == 0):
        num //= 2
    while(num % 3 == 0):
        num //= 3
    while(num % 5 == 0):
        num //= 5
    return num == 1

print(is_ugly(1))
    

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a, b = 12, 8
print("GCD:", gcd(a, b))
print("LCM:", lcm(a, b))


# finding extra candies
def find(list1, candies):
    maximum = max(list1)
    total = []
    # for i in list1:
    #     if candies+i >= maximum:
    #         total.append(True)
    #     else:
    #         total.append(False)
    total = [True if candies+i >= maximum else False for i in list1]
    return total

list1 = [2, 3, 5, 1, 4]
candies = 3
print(find(list1, candies))