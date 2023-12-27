from collections import deque
import random

global search_function
search_function = None

class BinaryNode:
    def __init__(self, value: str, left = None, right = None) -> None:
        self.value = value
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(self.value)

def build_node(tree: list[int]) -> BinaryNode:
    queue = deque()
    root = BinaryNode(tree[0])
    queue.append(root)
    i = 1
    while i <= len(tree)-2:
        node = queue.popleft()
        if tree[i]:
            node.left = BinaryNode(tree[i])
            queue.append(node.left)
        if tree[i+1]:
            node.right = BinaryNode(tree[i+1])
            queue.append(node.right)
        i += 2
    return root
