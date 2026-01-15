#!/usr/bin/env python3
# Zakaria Bouchaoui och Elias Bouchaoui

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        # Initialize an empty tree or a root with two empty children
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        # Check if value v exists in the tree
        if self.is_empty():
            return False
        if v == self.value():
            return True
        elif v < self.value():
            return self.lc().is_member(v)
        else:
            return self.rc().is_member(v)

    def size(self):
        # Count the number of nodes in the tree
        if self.is_empty():
            return 0
        return 1 + self.lc().size() + self.rc().size()

    def height(self):
        # Calculate the height of the tree
        if self.is_empty():
            return 0
        return 1 + max(self.lc().height(), self.rc().height())

    def preorder(self):
        # Preorder traversal: root, left, right
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        # Inorder traversal: left, root, right
        if self.is_empty():
            return []
        return self.lc().inorder() + [self.value()] + self.rc().inorder()

    def postorder(self):
        # Postorder traversal: left, right, root
        if self.is_empty():
            return []
        return self.lc().postorder() + self.rc().postorder() + [self.value()]

    def bfs_order_star(self):
        # Complete binary tree array (heap indexing): length 2^h - 1
        # Index i: left child at 2*i+1, right child at 2*i+2
        if self.is_empty():
            return []

        h = self.height()
        res = [None] * (2**h - 1)
        queue = [(self, 0)]  # (node, index in array)
        
        while queue:
            node, idx = queue.pop(0)
            if not node.is_empty():
                res[idx] = node.value()
                # Enqueue children with their heap indices
                queue.append((node.lc(), 2*idx + 1))
                queue.append((node.rc(), 2*idx + 2))
        
        return res

    def add(self, v):
        # Add a value to the BST
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        elif v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self

    def delete(self, v):
        # Remove a value from the BST
        if self.is_empty():
            return self

        if v < self.value():
            self.cons(self.lc().delete(v), self.rc())
            return self
        elif v > self.value():
            self.cons(self.lc(), self.rc().delete(v))
            return self

        # Node to delete found
        if self.lc().is_empty() and self.rc().is_empty():
            return BST()  # leaf node
        if self.lc().is_empty():
            return self.rc()  # only right child
        if self.rc().is_empty():
            return self.lc()  # only left child

        # Node has two children: use left maximum (predecessor) - "VÄNSTER först"
        predecessor = self.lc()._find_max()
        self.set_value(predecessor)
        self.cons(self.lc().delete(predecessor), self.rc())
        return self

    def _find_min(self):
        # Find the minimum value in the subtree
        if self.lc().is_empty():
            return self.value()
        return self.lc()._find_min()

    def _find_max(self):
        # Find the maximum value in the subtree
        if self.rc().is_empty():
            return self.value()
        return self.rc()._find_max()
