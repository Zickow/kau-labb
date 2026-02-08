#!/usr/bin/env python3 // Zakaria Bouchaoui o Elias Bouchaoui

import sys
import bst
import logging

log = logging.getLogger(__name__)

class AVL(bst.BST):
    def __init__(self, value=None):
        '''
        Initializes an empty tree if `value` is None, else a root with the
        specified `value` and two empty children.
        '''
        self.set_value(value)
        if not self.is_empty():
            self.cons(AVL(), AVL())

    def add(self, v):
        '''
        Adds the value `v` and returns the new (updated) tree.
        '''
        if self.is_empty():
            self.__init__(value=v)
            return self

        if v < self.value():
            self.cons(self.lc().add(v), self.rc())
        elif v > self.value():
            self.cons(self.lc(), self.rc().add(v))

        # If v is already present, nothing changes.
        return self.balance()

    def delete(self, v):
        '''
        Removes the value `v` from the tree and returns the new (updated) tree.
        If `v` is a non-member, the same tree is returned without modification.
        '''
        if self.is_empty():
            return self

        if v < self.value():
            self.cons(self.lc().delete(v), self.rc())
            return self.balance()
        if v > self.value():
            self.cons(self.lc(), self.rc().delete(v))
            return self.balance()

        # Found node to delete.
        lc = self.lc()
        rc = self.rc()

        if lc.is_empty() and rc.is_empty():
            return self._become_empty()
        if lc.is_empty():
            return rc
        if rc.is_empty():
            return lc

        # Two children: replace with predecessor (max in left subtree).
        pred = lc._max_value()
        new_left = lc.delete(pred)
        self.set_value(pred)
        self.cons(new_left, rc)
        return self.balance()

    def balance(self):
        '''
        AVL-balances around the node rooted at `self`.  In other words, this
        method applies one of the following if necessary: slr, srr, dlr, drr.
        '''
        if self.is_empty():
            return self

        bf = self.lc().height() - self.rc().height()

        if bf > 1:
            # Left heavy
            if self.lc().lc().height() >= self.lc().rc().height():
                return self.srr()
            return self.drr()

        if bf < -1:
            # Right heavy
            if self.rc().rc().height() >= self.rc().lc().height():
                return self.slr()
            return self.dlr()

        return self

    def slr(self):
        '''
        Performs a single-left rotate around the node rooted at `self`.
        '''
        if self.is_empty() or self.rc().is_empty():
            return self

        x = self
        y = self.rc()
        t2 = y.lc()

        # Rotate left: y becomes new root.
        x.cons(x.lc(), t2)
        y.cons(x, y.rc())
        return y

    def srr(self):
        '''
        Performs a single-right rotate around the node rooted at `self`.
        '''
        if self.is_empty() or self.lc().is_empty():
            return self

        x = self
        y = self.lc()
        t2 = y.rc()

        # Rotate right: y becomes new root.
        x.cons(t2, x.rc())
        y.cons(y.lc(), x)
        return y

    def dlr(self):
        '''
        Performs a double-left rotate around the node rooted at `self`.
        '''
        if self.is_empty():
            return self
        # Right-left case: rotate right child right, then rotate self left.
        self.cons(self.lc(), self.rc().srr())
        return self.slr()

    def drr(self):
        '''
        Performs a double-right rotate around the node rooted at `self`.
        '''
        if self.is_empty():
            return self
        # Left-right case: rotate left child left, then rotate self right.
        self.cons(self.lc().slr(), self.rc())
        return self.srr()

if __name__ == "__main__":
    log.critical("module contains no main module")
    sys.exit(1)
