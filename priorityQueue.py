"""
    Priority Queue:
    A Queue and Priority Queue both are used to save the data in datastructures.
    But this one have priority for all
    instead of removing at the front. It will remove based on the priority
    __init__
    is_empty
    push
    pop
    size

    Insert: O(log n)
    Remove: O(log n)
    peek: O(1)
"""

class PQueue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data, priority):
        index = 0
        while index < len(self.items) and self.items[index][1] >= priority:
            index += 1
        self.items.insert(index, (data, priority))
    
    def pop(self):
        if self.is_empty():
            raise ValueError("Queue Underflow")
        return self.items.pop(0)[0]
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if self.is_empty():
            raise ValueError("Queue Underflow")
        return self.items[0][0]
    
pq = PQueue()
pq.push("Ashol", 1)
pq.push("Anil", 10)
pq.push("Mani", 3)
pq.push("Gani", 7)
print(pq.peek())

print(pq.size())
while not pq.is_empty():
    # if val:=pq.pop():
    #     print(val)
    # break
    print(pq.pop())


# import heapq

# pq = []

# heapq.heappush(pq, 1)
# heapq.heappush(pq, 10)
# heapq.heappush(pq, 5)

# print(heapq.heappop(pq))
# print(heapq.heappop(pq))
# print(pq)