"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    # O(1)
    def add_to_head(self, value):
        newNode = ListNode(value) # create new ListNode

        # handles non-empty doubly linked lists
        if self.length > 0:
            self.length += 1 # increment length
            oldNode = self.head # save old head
            oldNode.prev = newNode # change old head prev value to new head
            newNode.next = oldNode # change new head next value to old head
            self.head = newNode # change head to newNode

        # handles empty doubly linked lists
        else:
            self.length += 1 # increment length
            self.head = newNode # set head and tail to newNode
            self.tail = newNode


    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    # O(1)
    def remove_from_head(self):

        # handles non-empty doubly linked lists with 2 or more nodes
        if self.length > 1:
            self.length -= 1 # decrement length
            oldNode = self.head # save old head

            self.head = oldNode.next # set head value to next node
            self.head.next = oldNode.next.next # set head next value to 2 nodes down from old head

            return oldNode.value # return old head

        # handles doubly linked lists with 1 value
        elif self.length == 1:
            self.length -= 1 # decrement length

            oldNode = self.head # save old head

            # set head and tail to None
            self.head = None
            self.tail = None
            
            return oldNode.value # return old head

        # handles empty double linked lists
        else:
            return # returns None

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    # O(1)
    def add_to_tail(self, value):
        newNode = ListNode(value) # create new ListNode

        # handles non-empty doubly linked lists
        if self.length > 0:
            self.length += 1 # increment length
            oldNode = self.tail # save old tail
            oldNode.next = newNode # change old tail next value to new tail
            newNode.prev = oldNode # change new tail next value to old head
            self.tail = newNode # change tail to newNode

        # handles empty doubly linked lists
        else:
            self.length += 1 # increment length
            self.head = newNode # set head and tail to newNode
            self.tail = newNode
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    # O(1)
    def remove_from_tail(self):

        # handles doubly linked lists with 2 or more nodes
        if self.length > 1:
            self.length -= 1 # decrement length
            oldNode = self.tail # save old tail

            self.tail = oldNode.prev # set tail value to prev node
            self.tail.next = None # set new tail next to None
            self.tail.prev = oldNode.prev.prev # set new tail prev value to 2 nodes up from old tail

            return oldNode.value # return old tail

        # handles doubly linked lists with 1 value
        elif self.length == 1:
            self.length -= 1 # decrement length

            oldNode = self.tail # save old tail

            # set head and tail to None
            self.head = None
            self.tail = None
            
            return oldNode.value # return old tail

        # handles empty double linked lists
        else:
            return # returns None
   
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    # O(n)
    def move_to_front(self, node):
        
        # handles doubly linked lists with 2 or more nodes
        if self.length > 1:
            current = self.head # start iterating at head

            # iterate over linked list until node argument is found
            while current is not node:
                current = current.next

            # set the prev node's next to node after current
            if current.prev is not None and current.next is not None:
                current.prev.next = current.next

            # set the next node's prev to node before current
            if current.prev is not None and current.next is not None:
                current.next.prev = current.prev

            oldHead = self.head # save old head
            oldHead.prev = current # set old head prev to current node
            current.prev = None # set current node's prev to None
            current.next = oldHead # set current node's next to old head
            self.head = current # set head to current node
        
        # handles all other doubly linked lists
        else:
            return
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    # O(n)
    def move_to_end(self, node):
        # handles doubly linked lists with 2 or more nodes
        if self.length > 1:
            current = self.head # start iterating at head

            # iterate over linked list until node argument is found
            while current is not node:
                current = current.next

            # handles case where the head is moved to end of 2 element doubly linked list
            if current == self.head:
                oldTail = self.tail # save old tail
                oldTail.next = current # set old tail next to current node
                self.head = current.next # set head to current's next node
                current.next = None # set current node's next to None
                current.prev = oldTail # set current node's prev to old tail
                self.tail = current # set tail to current node
            else:
                # set the prev node's next to node after current
                if current.prev is not None and current.next is not None:
                    current.prev.next = current.next

                # set the next node's prev to node before current
                if current.next is not None and current.next is not None:
                    current.next.prev = current.prev

                oldTail = self.tail # save old tail
                oldTail.next = current # set old tail next to current node
                current.next = None # set current node's next to None
                current.prev = oldTail # set current node's prev to old tail
                self.tail = current # set tail to current node
            
        # handles empty doubly linked lists
        else:
            return

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    # O(n)
    def delete(self, node):
        # handles doubly linked lists with 2 or more nodes
        if self.length > 1:
            current = self.head # start iterating at head
            self.length -= 1 # decrement length

            # iterate over linked list until node argument is found
            while current is not node:
                current = current.next

            # handles case when deleted node is head
            if current is self.head:
                current.next.prev = None # set new head's prev to None
                self.head = current.next # set head to new head
            
            # handles case when deleted node is in middle of list
            # set the prev node's next to node after current
            elif current.prev is not None and current.next is not None:
                current.prev.next = current.next

            # set the next node's prev to node before current
            elif current.prev is not None and current.next is not None:
                current.next.prev = current.prev
            
            # handles case when deleted node is tail
            elif current is self.tail:
                current.prev.next = None # set new tail's next to None
                self.tail = current.prev # set tail to new tail

        # handles case when list has 1 element
        elif self.length == 1:
            self.length -= 1
            self.head = None
            self.tail = None
            self.value = None
        
        # handles all other doubly linked lists
        else:
            return

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        max = 0
        current = self.head

        while current is not None:
            if max < current.value:
                max = current.value
            current = current.next
        
        return max