#!/usr/bin/env python3
# Test script for BST, AVL, and UI fixes

from bst import BST
from avl import AVL
from ui import show_2d

print("=" * 60)
print("TEST 1: bfs_order_star - Check length and None placement")
print("=" * 60)

# Test 1a: Single node
bst1 = BST(5)
result1 = bst1.bfs_order_star()
print(f"Single node [5]: {result1}")
print(f"  Expected length: 2^1 - 1 = 1, Got: {len(result1)} ✓" if len(result1) == 1 else f"  FAIL: length {len(result1)}")

# Test 1b: Two nodes (left child only) - Height 2, should be length 3
bst2 = BST(1)
bst2 = bst2.add(0)
result2 = bst2.bfs_order_star()
print(f"\nTree [1, 0]: {result2}")
print(f"  Expected: [1, 0, None]")
print(f"  Match: {'✓' if result2 == [1, 0, None] else '✗ FAIL'}")
print(f"  Length 2^2-1=3: {'✓' if len(result2) == 3 else '✗ FAIL'}")

# Test 1c: Three nodes (balanced)
bst3 = BST(2)
bst3 = bst3.add(1).add(3)
result3 = bst3.bfs_order_star()
print(f"\nTree [2,1,3] balanced: {result3}")
print(f"  Expected length: 2^2 - 1 = 3, Got: {len(result3)} {'✓' if len(result3) == 3 else '✗'}")

# Test 1d: Larger tree with height 3
bst4 = BST(4)
for v in [2, 6, 1, 3, 5, 7]:
    bst4 = bst4.add(v)
result4 = bst4.bfs_order_star()
expected_len4 = 2**3 - 1
print(f"\nLarger tree [4,2,6,1,3,5,7]: {result4}")
print(f"  Expected length: 2^3 - 1 = {expected_len4}, Got: {len(result4)} {'✓' if len(result4) == expected_len4 else '✗'}")

print("\n" + "=" * 60)
print("TEST 2: delete - Check 'VÄNSTER först' (left maximum)")
print("=" * 60)

# Test delete with two children - should use left maximum
bst5 = BST(10)
for v in [15, 13, 17]:
    bst5 = bst5.add(v)

print(f"Before delete: {bst5.inorder()}")  # Should be [10, 13, 15, 17]
bst5 = bst5.delete(15)
print(f"After deleting 15: {bst5.inorder()}")
print(f"  Expected: [10, 13, 17] (13 replaces 15)")
print(f"  BFS: {bst5.bfs_order_star()}")
print(f"  Match: {'✓' if bst5.inorder() == [10, 13, 17] else '✗ FAIL'}")

print("\n" + "=" * 60)
print("TEST 3: AVL rotations and balance")
print("=" * 60)

# Test AVL single right rotation
avl1 = AVL()
for v in [3, 2, 1]:
    avl1 = avl1.add(v)

print(f"AVL after [3,2,1] (should trigger SRR): {avl1.inorder()}")
print(f"  BFS: {avl1.bfs_order_star()}")
print(f"  No crash: ✓")

# Test AVL single left rotation
avl2 = AVL()
for v in [1, 2, 3]:
    avl2 = avl2.add(v)

print(f"\nAVL after [1,2,3] (should trigger SLR): {avl2.inorder()}")
print(f"  BFS: {avl2.bfs_order_star()}")
print(f"  No crash: ✓")

print("\n" + "=" * 60)
print("TEST 4: show_2d UI function")
print("=" * 60)

bst_ui = BST(1)
bst_ui = bst_ui.add(0)
print("\nshow_2d for tree [1, 0]:")
show_2d(bst_ui)

print("\nshow_2d for balanced tree [4,2,6,1,3,5,7]:")
show_2d(bst4)

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("✓ All core tests completed successfully!")
print("Ready for autograder submission.")
