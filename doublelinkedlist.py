"""
    creating one double linked list
    1. initialising
    2. is_empty
    3. insert_at_start() - rear end
    4. insert_at_end() - front end
    5. search()
    6. insert_after()
    7. print_list()
    8. iterator
    9. delete_first()
    10. delete_last()
    11. delete_item()

"""
from __future__ import annotations
from dataclasses import dataclass

@dataclass
class Node:
    prev : prev | None = None
    data : data | None = None
    next : next | None = None

class DLL:
    def __init__(self, rear=None):
        self.rear = rear

    # checking if the ddl is empty
    @property
    def _is_empty(self):
        return self.rear is None
    
    def insert_at_start(self, data):
        newNode = Node(None, data, self.rear)
        if not self._is_empty:
            self.rear.prev = newNode
        self.rear = newNode
    
    def insert_at_end(self, data):
        temp = self.rear
        if self.rear is not None:
            while temp.next is not None:
                temp = temp.next
        newNode = Node(temp, data, None)
        if temp is None:
            self.rear = newNode
        else:
            temp.next = newNode

    def insert_after(self, temp, data):
        if temp is not None:
            newNode = Node(temp, data, temp.next)
            if temp.next is not None:
                temp.next.prev = newNode
            temp.next = newNode

    def search(self, item):
        temp = self.rear
        while temp is not None:
            if temp.data == item:
                return temp
            temp = temp.next
        return None
    
    def print_lld(self):
        temp = self.rear
        while temp is not None:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def delete_first(self):
        if self.rear is not None:
            self.rear = self.rear.next
            if self.rear is not None:
                self.rear.prev = None

    def delete_last(self):
        if self.rear is None:
            pass
        elif self.rear.next is None:
            self.rear = None
        else:
            temp = self.rear
            while temp.next is not None:
                temp = temp.next
            temp.prev.next = None
    
    def delete_item(self, data):
        if self.rear is None:
            return
        
        # search for the node
        temp = self.search(data)

        if temp is None:
            return

        if temp.prev is None:
            self.delete_first()
            return

        if temp.next is None:
            self.delete_last()
            return
        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = None
        temp.next = None

#     def __iter__(self):
#         return DLLIterator(self.rear)

# class DLLIterator:
#     def __init__(self, rear):
#         self.current = rear
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if not self.current:
#             raise StopIteration
#         data = self.current.data
#         self.current = self.current.next
#         return data
        

#driver code
mylist = DLL()
mylist.insert_at_start(20)
mylist.insert_at_start(10)
mylist.insert_at_end(220)
mylist.insert_after(mylist.search(10),15)
mylist.delete_first()
mylist.delete_last()
# mylist.delete_item(15)
mylist.print_lld()


# for x in mylist:
#   print(x,end='<->')
# print()


