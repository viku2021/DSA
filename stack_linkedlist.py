class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedStack:
    def __init__(self):
        self.top = None
        self.length = 0

    def is_empty(self):
        return self.top is None

    def push(self,data):
        new_node =Node(data)
        new_node.next = self.top
        self.top = new_node
        self.length+=1


    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is Empty")
        
        popped_data = self.top.data
        self.top = self.top.next
        self.length -+1

        return popped_data

    def peek():
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.top.data

    def size(self):
        return self.length

    def display(self):
        if self.is_empty():
            print("Stack is Empty") 
            return
        
        current = self.top
        print("Top -> ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

stack = LinkedStack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
#print(f"Check stack is Empty: {stack.is_empty()}")
print("Linked Stack")
stack.display()

print(f"Pop : {stack.pop()}")
stack.display()