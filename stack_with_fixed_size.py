'''
A fixed-size stack is a type of stack data structure that has a predefined,
maximum capacity set at the time of its creation, which cannot be changed during runtime. 
It operates on the Last-In, First-Out (LIFO) principle.
'''

class BoundedStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def is_full(self):
        return len(self.items) == self.capacity
    
    def push(self, data):
        """Add element to top of stack - O(1)"""
        if self.is_full():
            raise OverflowError("Stack is full")
        self.items.append(data)
    
    def pop(self):
        """Remove and return top element - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def peek(self):
        """Return top element without removing - O(1)"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    def size(self):
        """Return number of elements - O(1)"""
        return len(self.items)
    
    def display(self):
        """Display stack from top to bottom"""
        if self.is_empty():
            print("Stack is empty")
            return
        print("Top -> ", end="")
        for i in range(len(self.items) - 1, -1, -1):
            print(self.items[i], end=" ")
        print("<- Bottom")



stack = BoundedStack(3)
stack.push(10)
stack.push(20)
stack.push(30)

try:
    stack.push(40)  
except OverflowError as e:
    print(f"Error: {e}")  



