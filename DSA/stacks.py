"""
    Creating a stack
    properties: reading/deleting at top
    top = -1 empty

    initializing
    is_empty
    push()
    pop()
    peek()
    size()

"""
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return IndexError("Stack is Empty")
        return self.items.pop()
    
    def peek(self):
        if self.is_empty():
            return IndexError("Stack is Empty")
        return self.items[-1]
    
    def size(self):
        return len(self.items)

    def print_stack(self):
        if not self.items:
            return
        return reversed(self.items)
s1 = Stack()
print("Is stack Empty?",s1.is_empty())
s1.push(10)
s1.push(22)
s1.push(30)
print(list(s1.print_stack()))
print("At the top is: ",s1.peek())
print("Deleted top element is: ",s1.pop())
print("At the top is: ",s1.peek())
print(s1.size())
print(list(s1.print_stack()))
