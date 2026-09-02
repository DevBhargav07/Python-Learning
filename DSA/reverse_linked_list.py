from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Node:
    data: int
    next_node: Node | None = None


class Linkedlist:
    """
        A representation of linked list
    """
    def __init__(self):
        self.head : Node | None = None
        self.tail : Node | None = None #speeds up the append() operation
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next_node
    
    def __repr__(self):
        return "->".join([str(data) for data in self])
    

    def append(self, data):
        if self.tail:
            self.tail.next_node = self.tail = Node(data)
        else:
            self.head = self.tail = Node(data)
    
    def extend(self, data):
        for data_ in data:
            self.append(data_)
    
def make_linkedlist(mylist):
    if not mylist:
        raise ValueError("List should not be empty")
    
    linkedlist = Linkedlist()
    linkedlist.extend(mylist)
    return linkedlist

def print_reverse(linkedlist):
    return "->".join([str(node) for node in reversed(tuple(linkedlist))])

linkedlist = make_linkedlist([1,2,99,42,121, 88, 65, 77, 99, 121, 1337])
to_reverse = print_reverse(linkedlist)
print(f'linkedlist is: {linkedlist}')
print(f'reversed_linked list is: {to_reverse}')
