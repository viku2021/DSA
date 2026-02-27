'''
A Stack is a linear data structure that follows the LIFO (Last In First Out) principle. 
The last element added is the first one to be removed. 
Real-world analogies: Stack of plates, browser back button, undo operations
'''

class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, data):
        """Add element to top of stack - O(1)"""
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



stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print("Stack after pushes:")
stack.display() 

print(f"\nPeek: {stack.peek()}")  
print(f"Pop: {stack.pop()}")      
print(f"Size: {stack.size()}")    

print("\nStack after pop:")
stack.display()  