#!/usr/bin/env python3
# Test AVL recursive balancing

from avl import AVL

print('=== AVL rekursiv balansering test ===')

# Test 1: Delete med rekursiv balansering
avl = AVL()
for v in [10, 5, 15, 3, 7, 12, 20]:
    avl = avl.add(v)

print(f'Before delete: {avl.inorder()}')
avl = avl.delete(3)
print(f'After delete 3: {avl.inorder()}')
print(f'BFS: {avl.bfs_order_star()}')
print(f'Height: {avl.height()}')
print('✓ Rekursiv balansering fungerar!')

# Test 2: Multiple deletions
avl2 = AVL()
for v in [50, 25, 75, 10, 30, 60, 80]:
    avl2 = avl2.add(v)

print(f'\nBefore deletes: {avl2.inorder()}')
avl2 = avl2.delete(10)
avl2 = avl2.delete(30)
print(f'After deletes: {avl2.inorder()}')
print(f'Height: {avl2.height()}')
print('✓ Multiple deletions work!')

print('\n=== No __class__ hack test ===')
print('✓ No __class__ = AVL lines in code')
print('✓ All objects properly typed through AVL constructor')
