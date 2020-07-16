from collections import deque

"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the Node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if we see that there is no left child,
                if self.left is None:
                    # then we can wrap the
                    # value in a BSTNode and park it
                    self.left = BSTNode(value)
                # otherwise there is a child
                else:            
                    # call the left child's insert method
                    self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go this Node's right child
            # if we see there is no right child, 
            if self.right is None:
                # then we can wrap the
                # value in a BSTNode and park it
                self.right = BSTNode(value)
            # otherwise there is a child
            else:
                # call the right child's insert method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare the target value with the value of the Node
        # if target < Node's value
        if target < self.value:
            # we need to go left
            # if we see that there is no left child,
            if self.left is None:
                # return False
                return False
            # otherwise there is a child
            else:            
                # call the left child's contains method
                return self.left.contains(target)
        # otherwise, target > Node's value
        else:
            # if target is Node's value
            if target == self.value:
                return True
            # we need to go this Node's right child
            # if we see there is no right child, 
            if self.right is None:
                # return False
                return False
            # otherwise there is a child
            else:
                # call the right child's contains method
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):

        # max value will be on the right-most leaf
        # recursively iterate through BST via right node until max value is found
        if self.right is None:
            return self.value
        return self.right.get_max()
                
    # Call the function `fn` on the value of each noden
    # Pre-order BST traversal
    # O(n)
    def for_each(self, fn):

        # Base case is when a leaf is reached
        if self.value is None:
            return

        # run callback on current node
        fn(self.value)

        # run callback on left subtree
        if self.left is not None:
            self.left.for_each(fn)

        # run callback on right subtree
        if self.right is not None:
            self.right.for_each(fn)

    def iterative_depth_first_for_each(self, fn):
        # DFT: LIFO
        # we'll use a stack
        stack = []
        stack.append(self)

        # so long as our stack has nodes on it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()

            # add the current node's right child first
            if current.right:
                stack.append(current.right)
            
            # add the current node's left child
            if current.left:
                stack.append(current.left)
            
            # call the anonymous function
            fn(current.value)

    def iterative_breadth_first_for_each(self, fn):
        # BFT: FIFO
        # we'll use a queue
        queue = deque()
        queue.append(self)
        
        # continue to traverse as long as there are nodes in the queue
        while len(queue) > 0:
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)

            fn(current)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # Base case is when a leaf is reached
        if self.value is None:
            return

        # run callback on left subtree
        if self.left:
            self.left.in_order_print(self.left)
        print(self.value)

        # run callback on right subtree
        if self.right:
            self.right.in_order_print(self.right)

        # # run callback on current node
        # print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
       # BFT: FIFO
        # we'll use a queue
        queue = deque()
        queue.append(self)
        
        # continue to traverse as long as there are nodes in the queue
        while len(queue) > 0:

            current = queue.popleft()
            print(current.value)

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # DFT: LIFO
        # we'll use a stack
        stack = []
        stack.append(self)

        # so long as our stack has nodes on it
        # there's more nodes to traverse
        while len(stack) > 0:
            # pop the top node from the stack
            current = stack.pop()

            # print current value
            print(current.value)

            # add the current node's right child first
            if current.right:
                stack.append(current.right)
            
            # add the current node's left child
            if current.left:
                stack.append(current.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)

        if node.left:
            node.left.for_each(print)
        
        if node.right:
            node.right.for_each(print)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        
        if node.right:
            self.post_order_dft(node.right)

        print(node.value)

# # Testing
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print(bst)
# bst.dft_print(bst)

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft(bst)
# print("in order")
# bst.in_order_print(bst)
# print("post order")
# bst.post_order_dft(bst)