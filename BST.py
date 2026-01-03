class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        
def insert(root, key):
    if root is None:
        return BSTNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def preorder(root):
    if root:
        print(root.key, end=" ")
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)
        
def postorder(root):    
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.key, end=" ")
        postorder(root.left)
        
def search(root, key):
    if root is None or root.key == key:
        return root
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def __str__(self, level=0):
        ret = "  " * level + str(self.key) + "\n"
        if self.left:
            ret += self.left.__str__(level + 1)
        if self.right:
            ret += self.right.__str__(level + 1)
        return ret
        
root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 70)
root = insert(root, 20)
root = insert(root, 40)

preorder(root)  # Output: 20 30 40 50 70