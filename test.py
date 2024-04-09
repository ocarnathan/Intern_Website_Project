class Binary_Tree:

    def __init__(self, root):
        self.root = root
        self.left_child = None
        self.right_child = None

    def insert_left_child(self, new_node):
        if self.left_child is None:
            self.left_child = Binary_Tree(new_node)

        else:
            subtree = Binary_Tree(new_node)
            subtree.left_child = self.left_child
            self.left_child = subtree
            

    def insert_right_child(self, new_node):
        if self.right_child is None:
            self.right_child = Binary_Tree(new_node)

        else:
            subtree = Binary_Tree(new_node)
            subtree.right_child = self.right_child
            self.right_child = subtree



bst = Binary_Tree(1)

bst.insert_left_child(2)
bst.insert_right_child(3)
bst.insert_left_child(2)
bst.insert_right_child(3)
bst.insert_left_child(2)
bst.insert_right_child(3)
bst.insert_left_child(3)
bst.insert_right_child(3)


print(bst.left_child.root)
