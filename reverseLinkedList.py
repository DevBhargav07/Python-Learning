from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    data: int
    next: Node | None = None

class LinkedList:
    def __init__(self):
        self.head : Node | None = None
        self.tail : Node | None = None

    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next

    def __repr__(self):
        return "->".join([str(d) for d in self])
    
    def append(self, data):
        if self.tail:
            self.tail.next = self.tail = Node(data)
        else:
            self.head = self.tail = Node(data)
    
    def extend(self, data):
        for d_ in data:
            self.append(d_)

def make_linkedlist(list1):
    if not list1:
        raise ValueError("List not be Empty")
    ll = LinkedList()
    ll.extend(list1)
    return ll

def reverseLL(ll):
    return "->".join([str(d) for d in reversed(tuple(ll))])

linkedlist = make_linkedlist([1,2,99,42,121, 88, 65, 77, 99, 121, 1337])
to_reverse = reverseLL(linkedlist)
print(f'linkedlist is: {linkedlist}')
print(f'reversed_linked list is: {to_reverse}')

