class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left, self.right = left, right
        self.height = 1


class AVL:
    def __init__(self):
        self.balance = 0
        self.root = None

    def get_height(self, node):
        if not node:
            return 0

        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        return 1 + max(left_height, right_height)

    def get_balance(self, node):
        if not node:
            return 0

        return self.get_height(node.left)-self.get_height(node.right)

    def rotate_right(self, y):
        x = y.left
        t2 = x.right
        x.right = y
        y.left = t2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return x

    def rotate_left(self, x):
        y = x.right
        t2 = y.left
        y.left = x
        x.right = t2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
            return self.root

        def insert_helper(node, value):
            if node is None:
                return TreeNode(value)

            if value < node.value:
                node.left = insert_helper(node.left, value)
            else:
                node.right = insert_helper(node.right, value)

            # ancestor node height
            node.height = 1 + max(self.get_height(node.left),
                                  self.get_height(node.right))

            balance = self.get_balance(node)

            # left left -> right rotation
            if balance > 1 and value < node.left.value:
                return self.rotate_right(node)

            # left right -> left-right rotation
            if balance > 1 and value > node.left.value:
                node.left = self.rotate_left(node.left)
                return self.rotate_right(node)

            # right right -> left rotation
            if balance < -1 and value > node.right.value:
                return self.rotate_left(node)

            # right left -> right-left rotation
            if balance < -1 and value < node.right.value:
                node.right = self.rotate_right(node.right)
                return self.rotate_left(node)

            return node

        self.root = insert_helper(self.root, value)

    def inorder_traversal(self):
        stack = []
        curr = self.root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            curr = stack.pop()
            print(curr.value, end=" ")
            curr = curr.right
        print()


nodes = [3, 2, 1]
tree = AVL()
for node in nodes:
    tree.insert(node)

tree.inorder_traversal()
