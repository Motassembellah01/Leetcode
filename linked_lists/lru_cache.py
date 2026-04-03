class Node:
    def __init__(self, key = None, value = None, left = None, right = None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.lib = {}
        self.head = Node()
        self.tail = Node()
        self.head.right = self.tail
        self.tail.left = self.head

        
    def get(self, key: int) -> int:
        
        if key in self.lib: # Je verifie que dans dictionnaire trouve key
            node = self.lib[key]
            self.removeNode(node)
            self.insertAfter(self.head, node)
            return node.value
        return -1


    def put(self, key: int, value: int):
        if key in self.lib:
            node = self.lib[key]
            self.removeNode(node)
            node.value = value
            self.insertAfter(self.head, node)
            return
        
        
        if len(self.lib) == self.capacity:
            itemToRemove = self.tail.left
            self.removeNode(itemToRemove)
            del self.lib[itemToRemove.key]

        node = Node(key, value)
        self.insertAfter(self.head, node)
        self.lib[key] = node


    def removeNode(self, node):
        node.right.left = node.left
        node.left.right = node.right
        

    def insertAfter(self, previous, node):
        node.left = previous
        node.right = previous.right
        node.left.right = node
        node.right.left = node

    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
