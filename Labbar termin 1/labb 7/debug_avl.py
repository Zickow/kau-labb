#!/usr/bin/env python3

import sys
sys.path.insert(0, r'c:\Users\Zakaria\Desktop\programering kau\Labbar termin 1\labb 7')

from avl import AVL

avl = AVL()
print(f"Initial: empty={avl.is_empty()}")

avl = avl.add(1)
print(f"After add(1): size={avl.size()}, inorder={avl.inorder()}, value={avl.value()}, empty={avl.is_empty()}")

avl = avl.add(2)
print(f"After add(2): size={avl.size()}, inorder={avl.inorder()}, value={avl.value()}")

avl = avl.add(3)
print(f"After add(3): size={avl.size()}, inorder={avl.inorder()}, value={avl.value()}")

avl = avl.add(4)
print(f"After add(4): size={avl.size()}, inorder={avl.inorder()}, value={avl.value()}")
