"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

# stack using arrays
# class Stack:
#     def __init__(self):
#         self.size = 0
#         self.storage = []

#     def __len__(self):
#         return len(self.storage)

#     def push(self, value):
#         self.storage.append(value)

#     def pop(self):
#         if len(self.storage) > 0:
#             last_value = self.storage[len(self.storage) - 1]
#             self.storage.pop()
#             return last_value
#         else:
#             return None

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next
    
    def set_next(self, new_next):
        self.next = new_next

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None

    # return stack length
    def __len__(self):

        # checks for empty stack
        if self.head is None and self.tail is None:
            return 0
        elif self.head is self.tail:
            return 1

        # start at the head
        current = self.head

        length = 2 # placeholder stack length variable

        # iterate through stack and count nodes
        while current.get_next() and current.get_next() is not self.tail:
            length += 1
            current = current.get_next()

        # length += 1 # at this point length is 1 short since it doesn't count the tail

        # return stack length
        return length

    def push(self, value):

        # create new Node with value argument
        new_node = Node(value)

        # handles empty stacks
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # handles all other stacks
        else:
            self.tail.set_next(new_node) # point next attribute to new Node
            self.tail = new_node # set tail attribute to new Node

    def pop(self):
        # handles empty linked lists
        if self.head is None and self.tail is None:
            return
        elif self.head is self.tail:
            value = self.tail.get_value()
            self.head = None
            self.tail = None
            return value

        # start at the head
        current = self.head

        while current.get_next() and current.get_next() is not self.tail:
            current = current.get_next()

        # at this point, `current` is the node right before the tail
        value = self.tail.get_value()
        # move self.tail to the Node right before
        self.tail = current
        # set the tail next attribute to be None
        self.tail.set_next(None)

        return value