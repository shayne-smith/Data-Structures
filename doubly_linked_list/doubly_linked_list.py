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
    def add_to_tail(self, value):
        pass
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        pass
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        pass
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        pass

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass