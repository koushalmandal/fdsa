class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def _insert(self, node, data):
        if node is None:
            return TreeNode(data)
        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)
        return node

    def insert(self, data):
        self.root = self._insert(self.root, data)

    def _in_order(self, node):
        if node:
            self._in_order(node.left)
            print(node.data, end=" ")
            self._in_order(node.right)

    def in_order_traversal(self):
        self._in_order(self.root)
        print()


tree = BinaryTree()
tree.insert(50)
tree.insert(30)
tree.insert(70)
tree.insert(20)
tree.insert(40)
tree.insert(60)
tree.insert(80)
print("In-order Traversal:", end=" ")
tree.in_order_traversal()

