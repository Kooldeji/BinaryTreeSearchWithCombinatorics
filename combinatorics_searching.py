from typing import Optional
from tree import *

no_branches = 2
addr_space = 30

def search(node: BinaryNode, action):
    cur_idx = 0
    max_depth = 0

    while cur_idx < (2**max_depth):
        path_length, next_idx = traverse_path(node, max_depth, cur_idx, action)
        max_depth = max(path_length, max_depth)
        cur_idx = next_idx


def get_path(n: int, row: int, col: int):
    '''
    Given a n, row idx and col idx.
    Gen the row_idx of the col_idx'th combination of size n
    i.e Given n = 3, row = 2, col = 1
        000 = 0
        001 = 1
        010 = 2  <----
         ^
        011 = 3
        100 = 4
        101 = 5
        110 = 6 
        111 = 7

        return ==> 1

        Constraints: 
        - row < 2^addr_space
    '''
    return (row & (1 << col)) >> col

def traverse_path(node: BinaryNode, max_depth: int, cur_idx: int, action) -> tuple[int, int]:
    next_node: Optional[BinaryNode] = node
    path_length: int = 0
    action(next_node)
    for idx in range(max_depth-1, -1, -1):
        decision = get_path(max_depth, cur_idx, idx)
        if decision == 1:
            next_node = next_node.right
        else:
            next_node = next_node.left
        path_length += 1
        if not next_node:
            break
        action(next_node)

    # Left Node follower, to find the new path length
    next_idx = cur_idx
    while next_node and (next_node.left or next_node.right):
        path_length += 1
        next_idx *= 2
        if next_node.left:
            next_node = next_node.left
        else:
            next_node = next_node.right
            next_idx += 1
        action(next_node)
    if max_depth > path_length:
        skip = 2**(max_depth - path_length)
    else:
        skip = 1
    
    return path_length, next_idx + skip


def test(tree, name: str):
    print("-"*50, "test(", name, ")", "-"*50)
    print("tree:", tree)
    validations = set()
    def touch(node):
        if node:
            validations.add(node.value)
        print(sorted(validations))
    root = build_node(tree)
    search(root, lambda x: touch(x))

def full(n):
    tree = [i+1 for i in range(n)]
    test(tree, "full - "+ str(n))

def left(n):
    tree = [1]
    for i in range(n):
        tree.append(i+2)
        tree.append(None)
    test(tree, "left - "+ str(n))

def right(n):
    tree = [1]
    for i in range(n):
        tree.append(None)
        tree.append(i+2)
    test(tree, "right - "+ str(n))

def rand(n):
    tree = [1]
    no_nodes = 1
    count = 1
    while no_nodes > 0 and count < n:
        no_nodes -= 1
        r = random.randrange(0, 3)
        if r == 0 or r == 2:
            count += 1
            tree.append(count)
            no_nodes += 1
        else:
            tree.append(None)
        if r == 1 or r == 2:
            count += 1
            tree.append(count)
            no_nodes += 1
        else:
            tree.append(None)
    test(tree, "rand - "+str(n))

def fixed(tree):
    test(tree, "fixed")


# full(1)
# full(3)
# full(31)
            
# left(3)
# left(30)

 
# right(3)
# right(30)
            
# for i in range(20):
#     rand(5)
    
rand(40)
    
# fixed([1, None, 2, 3, 4, 5, None])

'''
          x
         /  \
        x    x
       / \   /  \
      x   x x    x
               / \
              x   x
       x
     /  \
    x    x
        / \
       x   x
'''
'''
       x
      / 
     x
    / 
   x 
  /
 x
'''


