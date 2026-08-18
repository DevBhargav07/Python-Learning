from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
  data: int
  left: Node | None = None
  right: Node | None = None

def insert(root, key):
  if root is None:
    return Node(key)
  if key < root.data:
    root.left = insert(root.left, key)
  else:
    root.right = insert(root.right, key)
  return root

def search(root, key):
  if root is None or root.data == key:
    return root
  if root.data > key:
    return search(root.left, key)
  return search(root.right, key)

#finding the minvalNode
def minValNode(root):
  curr = root
  while curr.left is not None:
    curr = curr.left
  return curr

def deleteNode(root, key):
  if root is None:
    return root
  
  if root.data > key:
    root.left = deleteNode(root.left, key)
  elif root.data < key:
    root.right = deleteNode(root.right, key)
  else:
    # if having no left children
    if root.left is None:
      temp = root.right
      root = None
      return temp
    # having no right childre
    elif root.right is None:
      temp = root.left
      root = None
      return temp
    # having both children
    temp = minValNode(root.right)
    root.data = temp.data
    root.right = deleteNode(root.right, temp.data)
  return root

def height(root):
    if root is None:
        return 0
    left = height(root.left)
    right = height(root.right)
    return max(left, right) + 1

def inorder(root):
  if root is None:
    return
  inorder(root.left)
  print(root.data,end=" ")
  inorder(root.right)

def preorder(root):
  if root is None:
    return
  print(root.data,end=" ")
  preorder(root.left)
  preorder(root.right)

def postorder(root):
  if root is None:
    return
  postorder(root.left)
  postorder(root.right)
  print(root.data, end=" ")


root = None
keys = [5,3,7,1,4,6,8]
for key in keys:
  root = insert(root, key)

inorder(root)
print()
preorder(root)
print()
postorder(root)
print()
if search(root, 12) is None:
  print('Not found')
else:
  print('found')
root = deleteNode(root, 7)
inorder(root)
print()
preorder(root)
print()
print(f'Height of the tree is: {height(root)}')
