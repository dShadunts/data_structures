class BinaryNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


# https://stackoverflow.com/questions/2598437/how-to-implement-a-binary-tree
class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def add(self, val):
        if self.root is None:
            self.root = BinaryNode(val)
        else:
            self._add(val, self.root)

    def _add(self, val, node):
        if val < node.data:
            if node.left is not None:
                self._add(val, node.left)
            else:
                node.left = BinaryNode(val)
        else:
            if node.right is not None:
                self._add(val, node.right)
            else:
                node.right = BinaryNode(val)
        self.size += 1

    def find(self, val, node):
        if self.root is None:
            return None
        elif val == node.data:
            return node
        elif val < node.data and node.left is not None:
            self.find(val, node.left)
        elif val > node.data and node.right is not None:
            self.find(val, node.right)

    # returns array of nodes by inorder traversal
    def inorder(self, node):
        if node is None:
            return []
        left = self.inorder(node.left)
        right = self.inorder(node.right)
        return left + [node.data] + right

    # get height of the bst
    def get_height(self):
        return self._get_height(self.root)

    def _get_height(self, node):
        if node is None: return 0
        return max(1 + self._get_height(node.left), 1 + self._get_height(node.right))

    # Prints kth maximum value in a binary search tree
    # reverse inorder traversal will return nodes sorted in desc order
    def kth_maximum(self, node, k):
        if k <= 0 or node is None:
            return k
        k = self.kth_maximum(node.right, k)
        k -= 1
        if k == 0:
            print node.data
        return self.kth_maximum(node.left, k)

    # Find nodes at "k" distance from the root
    def kth_level(self, node, k, nodes=[]):
        if node is not None:
            if k == 0:
                nodes += [node]
            else:
                self.kth_level(node.left, k - 1, nodes=nodes)
                self.kth_level(node.right, k - 1, nodes=nodes)
        return nodes

    # Fills ancestors of a given target node into the result array
    # returns true if node is found in the tree
    def fill_ancestors(self, node, target, result):
        if node is None:
            return False
        if node.data == target:
            return True
        in_left = self.fill_ancestors(node.left, target, result)
        in_right = False
        if not in_left:
            in_right = self.fill_ancestors(node.right, target, result)
        if in_left or in_right:
            result += [node]
        return in_left or in_right
