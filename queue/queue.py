"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""

# queue using arrays
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) > 0:
#             first_value = self.storage[0]
#             self.storage.pop(0)
#             return first_value
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

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    # return queue length
    def __len__(self):

        # checks for empty queue
        if self.head is None and self.tail is None:
            return 0
        # checks for single-element queue
        elif self.head is self.tail:
            return 1

        # start at the head
        current = self.head

        length = 1 # placeholder queue length variable

        # iterate through queue and count nodes
        while current.get_next() and current.get_next is not self.tail:
            length += 1
            current = current.get_next()

        # return queue length
        return length
    
    def enqueue(self, value):
        
        # create a new Npde with value arguments
        new_node = Node(value)

        # handles empty queues
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        # handles all other queues
        else:
            self.tail.set_next(new_node) # point next attribute to new Node
            self.tail = new_node # set tail attribute to new Node

    def dequeue(self):
        # handles empty queue
        if self.head is None and self.tail is None:
            return
        
        # handles single-element queue
        if not self.head.get_next():
            head = self.head
            # delete the queue's head reference
            self.head = None
            # also delete the queue's tail reference
            self.tail = None
            return head.get_value()

        val = self.head.get_value()
        # set self.head to the Node after the head
        self.head = self.head.get_next()
        return val

