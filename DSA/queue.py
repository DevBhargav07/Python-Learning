""" 
    Queue Using List
    Define __init__
    is_empty
    enqueue
    dequeue
    get_front
    get_rear
    size

    Insert: O(1)
    Delete: O(1)
    peek:   O(1)
"""

class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            self.items.pop(0)
        else:
            raise ValueError("Queue Underflow")
        
    def get_front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise ValueError("Queue Underflow")
        
    def get_rear(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise ValueError("Queue Underflow")
    def size(self):
        return len(self.items)

    def printQueue(self):
        print("->".join([str(val) for val in self.items]))
    
q = Queue()
print(q.size())
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
print(f"The First element added and to be deleted is: {q.get_front()}")
print(f"The Last element added and to be deleted is: {q.get_rear()}")
q.dequeue()
print(q.size())
# print()
q.printQueue()

# basically overflow will happen if we put any limit for the enqueue


        
    

    
