class AVLNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1
    
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self):
        return self.get_height(self.left) - self.get_height(self.right)

    def left_rotate(self):
        new_root = self.right
        T2 = new_root.left
        # Perform rotation
        new_root.left = self
        self.right = T2
        # Update heights
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root

    def right_rotate(self):
        new_root = self.left
        T3 = new_root.right
        # Perform rotation
        new_root.right = self
        self.left = T3
        # Update heights
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        new_root.height = 1 + max(self.get_height(new_root.left), self.get_height(new_root.right))
        return new_root
        
    def insert(self, data):
        if data < self.data:
            if self.left is None:
                self.left = AVLNode(data)
            else:
                self.left = self.left.insert(data)
        else:
            if self.right is None:
                self.right = AVLNode(data)
            else:
                self.right = self.right.insert(data)
        
        self.height = 1 + max(self.get_height(self.left), self.get_height(self.right))
        balance = self.get_balance()
        
        # Left Left Case
        if balance > 1 and data < self.left.data:
            return self.right_rotate()
        
        # Right Right Case
        if balance < -1 and data > self.right.data:
            return self.left_rotate()
        
        # Left Right Case
        if balance > 1 and data > self.left.data:
            self.left = self.left.left_rotate()
            return self.right_rotate()
        
        # Right Left Case
        if balance < -1 and data < self.right.data:
            self.right = self.right.right_rotate()
            return self.left_rotate()
        
        return self
        
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)
        
def inorder(root):
    if root:
        inorder(root.left)
        print(root.data, end=" ")
        inorder(root.right)
                
def postorder(root):    
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data, end=" ")

def level_order(root):
    if not root:
        return
    queue = [root]
    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

            
tree = AVLNode(10)
tree = tree.insert(20)
tree = tree.insert(30)
tree = tree.insert(40)
tree = tree.insert(50)
tree = tree.insert(60)
print("Preorder traversal of the constructed AVL tree is:")
preorder(tree)
print("\nInorder traversal of the constructed AVL tree is:")
inorder(tree)
print("\nPostorder traversal of the constructed AVL tree is:")
postorder(tree)
print("\nLevel order traversal of the constructed AVL tree is:")
level_order(tree)