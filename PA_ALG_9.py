# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
# Binary search tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None
    # Insert a node into the binary search tree
    def insert_node(self, value):
        new_node = Node(value)
        # If the tree is empty, the new node becomes the root node
        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                # If the new node's value is less than the current node's value, move to the left subtree
                if value < current_node.value:
                    if current_node.left is None:
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                # If the new node's value is greater than or equal to the current node's value, move to the right subtree
                else:
                    if current_node.right is None:
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
bst = BinarySearchTree()
bst.insert_node(5)
bst.insert_node(3)
bst.insert_node(8)
bst.insert_node(4)
bst.insert_node(1)
bst.insert_node(9)
def print_inorder(node):
    if node:
        print_inorder(node.left)
        print(node.value)
        print_inorder(node.right)
print_inorder(bst.root)
