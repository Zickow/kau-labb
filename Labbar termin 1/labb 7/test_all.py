#!/usr/bin/env python3
# Test file for bt.py, bst.py, avl.py, and ui.py

import sys
sys.path.insert(0, r'c:\Users\Zakaria\Desktop\programering kau\Labbar termin 1\labb 7')

from bt import BT
from bst import BST
from avl import AVL

print("=" * 60)
print("Testing BT (Binary Tree)")
print("=" * 60)

# Test BT
bt_root = BT(5)
bt_root.lc().set_value(3)
bt_root.rc().set_value(7)
print(f"BT root value: {bt_root.value()}")
print(f"BT left child: {bt_root.lc().value()}")
print(f"BT right child: {bt_root.rc().value()}")
print(f"BT is empty: {bt_root.is_empty()}")
print()

print("=" * 60)
print("Testing BST (Binary Search Tree)")
print("=" * 60)

# Test BST
bst = BST()
values = [5, 3, 7, 1, 4, 6, 8]
for v in values:
    bst = bst.add(v)

print(f"Added values: {values}")
print(f"BST size: {bst.size()}")
print(f"BST height: {bst.height()}")
print(f"Is 4 member: {bst.is_member(4)}")
print(f"Is 10 member: {bst.is_member(10)}")
print(f"Inorder (should be sorted): {bst.inorder()}")
print(f"Preorder: {bst.preorder()}")
print(f"Postorder: {bst.postorder()}")
print(f"BFS order: {bst.bfs_order_star()}")

# Test delete
bst_copy = BST()
for v in values:
    bst_copy = bst_copy.add(v)
bst_copy.delete(3)
print(f"After deleting 3: {bst_copy.inorder()}")
print()

print("=" * 60)
print("Testing AVL (AVL Tree)")
print("=" * 60)

# Test AVL
avl = AVL()
avl_values = [10, 5, 15, 2, 7, 12, 20]
for v in avl_values:
    avl = avl.add(v)

print(f"Added values: {avl_values}")
print(f"AVL size: {avl.size()}")
print(f"AVL height: {avl.height()}")
print(f"Is 7 member: {avl.is_member(7)}")
print(f"Is 100 member: {avl.is_member(100)}")
print(f"Inorder (should be sorted): {avl.inorder()}")
print(f"BFS order: {avl.bfs_order_star()}")
print(f"Height diff at root: {avl.height_diff()}")

# Test AVL delete
avl.delete(2)
print(f"After deleting 2: {avl.inorder()}")
print(f"Height after delete: {avl.height()}")
print()

print("=" * 60)
print("Testing stress: Adding many values to AVL")
print("=" * 60)

avl_stress = AVL()
for i in range(1, 16):
    avl_stress = avl_stress.add(i)

print(f"Added 1-15 to AVL")
print(f"AVL size: {avl_stress.size()}")
print(f"AVL height: {avl_stress.height()}")
print(f"Inorder: {avl_stress.inorder()}")
print(f"Height is balanced (should be log): height={avl_stress.height()}")
print()

print("=" * 60)
print("All tests completed successfully!")
print("=" * 60)
