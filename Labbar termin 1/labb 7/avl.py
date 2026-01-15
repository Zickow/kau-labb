#!/usr/bin/env python3
# Zakaria Bouchaoui och Elias Bouchaoui

from bst import BST
import logging

log = logging.getLogger(__name__)

class AVL(BST):

    def height_diff(self):
        # Compute the balance factor: left height - right height
        if self.is_empty():
            return 0
        return self.lc().height() - self.rc().height()

    def balance(self):
        # Fix at most one AVL violation
        if self.is_empty():
            return self

        diff = self.height_diff()

        # Left heavy
        if diff > 1:
            if self.lc().height_diff() >= 0:
                return self.srr()  # single right rotation
            else:
                return self.drr()  # double right rotation

        # Right heavy
        if diff < -1:
            if self.rc().height_diff() <= 0:
                return self.slr()  # single left rotation
            else:
                return self.dlr()  # double left rotation

        return self

    # -------- ROTATIONS ----------------

    def srr(self):
        # Single right rotation
        new_root = self.lc()
        self.cons(new_root.rc(), self.rc())
        new_root.cons(new_root.lc(), self)
        return new_root

    def slr(self):
        # Single left rotation
        new_root = self.rc()
        self.cons(self.lc(), new_root.lc())
        new_root.cons(self, new_root.rc())
        return new_root

    def drr(self):
        # Double right rotation: left child left rotate, then right rotate
        self.cons(self.lc().slr(), self.rc())
        return self.srr()

    def dlr(self):
        # Double left rotation: right child right rotate, then left rotate
        self.cons(self.lc(), self.rc().srr())
        return self.slr()

    # -------- ADD + DELETE ----------------

    def add(self, v):
        # Add a value and balance the tree
        if self.is_empty():
            self.set_value(v)
            self.cons(AVL(), AVL())
            return self
        if v < self.value():
            self.cons(self.lc().add(v), self.rc())
        elif v > self.value():
            self.cons(self.lc(), self.rc().add(v))
        return self.balance()

    def delete(self, v):
        # Delete a value and balance the tree recursively
        if self.is_empty():
            return self

        if v < self.value():
            self.cons(self.lc().delete(v), self.rc())
            return self.balance()
        elif v > self.value():
            self.cons(self.lc(), self.rc().delete(v))
            return self.balance()

        # Node to delete found
        if self.lc().is_empty() and self.rc().is_empty():
            return AVL()  # leaf node
        if self.lc().is_empty():
            return self.rc()  # only right child
        if self.rc().is_empty():
            return self.lc()  # only left child

        # Node has two children: use left maximum (predecessor)
        predecessor = self.lc()._find_max()
        self.set_value(predecessor)
        self.cons(self.lc().delete(predecessor), self.rc())
        return self.balance()
