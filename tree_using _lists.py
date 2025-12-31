class ListTree:
    def __init__(self, size):
        self.tree = [None] * size
        self.last_used_index = 0
        self.max_size = size
        
    def insert(self, value):
        if self.last_used_index >= self.max_size - 1:
            return "The tree is full"
        self.last_used_index += 1
        self.tree[self.last_used_index] = value
        return "Value inserted successfully"
    
    def search(self, value):
        for i in range(1, self.last_used_index + 1):
            if self.tree[i] == value:
                return f"Value found at index {i}"
        return "Value not found in the tree"
        
    def preordertraversal(self, index):
        if index > self.last_used_index:
            return
        print(self.tree[index])
        self.preordertraversal(2 * index)
        self.preordertraversal(2 * index + 1)

        
newBt = ListTree(9)
print(newBt.insert("Drinks"))
print(newBt.insert("Hot"))
print(newBt.insert("Cold"))  
print(newBt.insert("Tea"))
print(newBt.insert("Coffee"))
  
print(newBt.search("Cold"))

print(newBt.preordertraversal(1))
