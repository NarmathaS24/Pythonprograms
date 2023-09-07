class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert(data, node.right)

    def search(self, data):
        if not self.root:
            return False
        else:
            return self._search(data, self.root)

    def _search(self, data, node):
        if data == node.data:
            return True
        elif data < node.data and node.left is not None:
            return self._search(data, node.left)
        elif data > node.data and node.right is not None:
            return self._search(data, node.right)
        return False

    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data)
            self.inorder_traversal(node.right)
bst = BST()
bst.insert(50)
bst.insert(30)
bst.insert(20)
bst.insert(40)
bst.insert(70)
bst.insert(60)
bst.insert(80)

bst.inorder_traversal(bst.root)
print(bst.search(40))
print(bst.search(100))


