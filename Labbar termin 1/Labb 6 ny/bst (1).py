#!/usr/bin/env python3  // Zakaria Bouchaoui o Elias Bouchaoui

import bt
import sys
import logging

log = logging.getLogger(__name__)

class BST(bt.BT):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(BST(), BST())

    def is_member(self, v):
        '''
        Returns true if the value `v` is a member of the tree.
        '''
        if self.is_empty():
            return False
        if v == self.value():
            return True
        if v < self.value():
            return self.lc().is_member(v)
        return self.rc().is_member(v)

    def size(self):
        '''
        Returns the number of nodes in the tree.
        '''
        if self.is_empty():
            return 0
        return 1 + self.lc().size() + self.rc().size()

    def height(self):
        '''
        Returns the height of the tree.
        '''
        # Height criteria for this lab:
        #   empty tree -> 0
        #   single-node tree -> 1
        if self.is_empty():
            return 0
        return 1 + max(self.lc().height(), self.rc().height())

    def preorder(self):
        '''
        Returns a list of all members in preorder.
        '''
        if self.is_empty():
            return []
        return [self.value()] + self.lc().preorder() + self.rc().preorder()

    def inorder(self):
        '''
        Returns a list of all members in inorder.
        '''
        if self.is_empty():
            return []
        return self.lc().inorder() + [self.value()] + self.rc().inorder()

    def postorder(self):
        '''
        Returns a list of all members in postorder.
        '''
        if self.is_empty():
            return []
        return self.lc().postorder() + self.rc().postorder() + [self.value()]

    def bfs_order_star(self):
        '''
        Returns a list of all members in breadth-first search* order, which
        means that empty nodes are denoted by "stars" (here the value None).

        For example, consider the following tree `t`:
                    10
              5           15
           *     *     *     20

        The output of t.bfs_order_star() should be:
        [ 10, 5, 15, None, None, None, 20 ]
        '''
        h = self.height()
        if h == 0:
            return []

        # Level-order traversal that includes placeholders (None) for
        # non-existing nodes up to the full height of the tree.
        res = []
        q = [(self, 1)]  # (node, current_level), levels start at 1
        while q:
            node, lvl = q.pop(0)
            if lvl > h:
                continue

            if node.is_empty():
                res.append(None)
                if lvl < h:
                    q.append((BST(), lvl + 1))
                    q.append((BST(), lvl + 1))
                continue

            res.append(node.value())
            if lvl < h:
                q.append((node.lc(), lvl + 1))
                q.append((node.rc(), lvl + 1))

        return res

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.  If `v` is
        already a member, the same tree is returned without any modification.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self
        if v < self.value():
            return self.cons(self.lc().add(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().add(v))
        return self
    
    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if self.is_empty():
            return self

        if v < self.value():
            return self.cons(self.lc().delete(v), self.rc())
        if v > self.value():
            return self.cons(self.lc(), self.rc().delete(v))

        # Found node to delete.
        lc = self.lc()
        rc = self.rc()

        # Case: leaf
        if lc.is_empty() and rc.is_empty():
            return self._become_empty()

        # Case: one child
        if lc.is_empty():
            return rc
        if rc.is_empty():
            return lc

        # Case: two children
        # Replace with predecessor (largest value in left subtree).  This
        # follows the lab rule "if possible, always pick left".
        pred = lc._max_value()
        new_left = lc.delete(pred)
        self.set_value(pred)
        return self.cons(new_left, rc)

    def _become_empty(self):
        """Turns this node into an empty tree and returns self."""
        self.set_value(None)
        self.set_lc(None)
        self.set_rc(None)
        return self

    def _max_value(self):
        """Returns the maximum value in a non-empty tree."""
        if self.rc().is_empty():
            return self.value()
        return self.rc()._max_value()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
