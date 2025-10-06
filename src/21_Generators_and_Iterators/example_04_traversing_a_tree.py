#!/usr/bin/env python

class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.value = value
        self.right = right

    def traverse(self):
        if self.left:
            yield from self.left.traverse()
        yield self.value
        if self.right:
            yield from self.right.traverse()


if __name__ == "__main__":
    bl_ = Node(left=Node(12), value=1, right=Node(3))
    bl = Node(left=bl_, value=5, right=Node(6))

    br_ = Node(left=Node(2), value=8)
    br = Node(left=Node(9), value=7, right=br_)

    tree = Node(left=bl, value=11, right=br)
    print(list(tree.traverse()))

