class Node:
    def __init__(self, value): 
        self.value = value
        self.next = None
        
class LinkedQueue:
    def __init__(self):
        self.head=None
        self.tail=None
        self.length=0
        
    def is_empty(self):
        return self.length == 0
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        removed_value = self.head.value
        self.head = self.head.next
        self.length -= 1
        if self.is_empty():
            self.tail = None
        return removed_value
    
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        
    def __str__(self):
        result = []
        Q = LinkedQueue()
        Q.enqueue(self)

        while not Q.is_empty():
            current = Q.dequeue()
            result.append(str(current.value))
            if current.leftChild:
                Q.enqueue(current.leftChild)
            if current.rightChild:
                Q.enqueue(current.rightChild)
        return " ".join(result)

        
        
newBt=TreeNode("Drinks")
leftChild=TreeNode("Hot")
rightChild=TreeNode("Cold")

newBt.leftChild=leftChild
newBt.rightChild=rightChild

def preorder_traversal(node):
    if node:
        print(node.value)
        preorder_traversal(node.leftChild)
        preorder_traversal(node.rightChild)
        
# preorder_traversal(newBt)

def inorder_traversal(node):
    if node:
        inorder_traversal(node.leftChild)
        print(node.value)
        inorder_traversal(node.rightChild)

# inorder_traversal(newBt)

def postorder_traversal(node):
    if node:
        postorder_traversal(node.leftChild)
        postorder_traversal(node.rightChild)
        print(node.value)
        
# postorder_traversal(newBt)

def levelorder_traversal(node):
    if not node:
        return
    
    else:
        Q=LinkedQueue()
        Q.enqueue(node)
        while not Q.is_empty():
            current_node=Q.dequeue()
            print(current_node.value)
            if current_node.leftChild:
                Q.enqueue(current_node.leftChild)
            if current_node.rightChild:
                Q.enqueue(current_node.rightChild)
                
# levelorder_traversal(newBt)


def searchnode(node, target):
    if not node:
        return False
    else:
        Q=LinkedQueue()
        Q.enqueue(node)
        while not Q.is_empty():
            current_node = Q.dequeue()
            if current_node.value == target:
                return True
            if current_node.leftChild:
                Q.enqueue(current_node.leftChild)   
            if current_node.rightChild:
                Q.enqueue(current_node.rightChild)
        return False
    
# print(searchnode(newBt, "Hot"))

def insertnode(node,value):
        newnode = TreeNode(value)
        if not node:
            return
        
        else:
            Q=LinkedQueue()
            Q.enqueue(node)
            while not Q.is_empty():
                current_node = Q.dequeue()
                
                # Check left child
                if current_node.leftChild:
                    Q.enqueue(current_node.leftChild)
                else:
                    current_node.leftChild = newnode
                    return "Successfully inserted"
                
                # Check right child
                if current_node.rightChild:
                    Q.enqueue(current_node.rightChild)
                else:
                    current_node.rightChild = newnode
                    return "Successfully inserted"
                
print(insertnode(newBt, "Juice"))

def get_deepest_node(node):
    if not node:
        return None
    
    Q=LinkedQueue()
    Q.enqueue(node)
    deepest_node = None
    
    while not Q.is_empty():
        deepest_node = Q.dequeue()
        
        if deepest_node.leftChild:
            Q.enqueue(deepest_node.leftChild)
        if deepest_node.rightChild:
            Q.enqueue(deepest_node.rightChild)
    
    return deepest_node
# print(get_deepest_node(newBt).value)
print(newBt)

def delete_deepest_node(node, d_node):
    if not node:
        return
    
    Q=LinkedQueue()
    Q.enqueue(node)
    
    while not Q.is_empty():
        current_node = Q.dequeue()
        
        if current_node is d_node:
            current_node = None
            return
        
        if current_node.rightChild:
            if current_node.rightChild is d_node:
                current_node.rightChild = None
                return
            else:
                Q.enqueue(current_node.rightChild)
        
        if current_node.leftChild:
            if current_node.leftChild is d_node:
                current_node.leftChild = None
                return
            else:
                Q.enqueue(current_node.leftChild)