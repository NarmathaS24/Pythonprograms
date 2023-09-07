# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Binary tree class
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
    # In-order traversal
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value)
            self.inorder_traversal(node.right)
    # Pre-order traversal
    def preorder_traversal(self, node):
        if node:
            print(node.value)
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    # Post-order traversal
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value)

# Create a binary tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# In-order traversal
print("In-order traversal:")
tree.inorder_traversal(tree.root)

# Pre-order traversal
print("Pre-order traversal:")
tree.preorder_traversal(tree.root)

# Post-order traversal
print("Post-order traversal:")
tree.postorder_traversal(tree.root)
