# Convert a BST to a sorted circular doubly-linked list in-place. 
# Think of the left and right pointers as synonymous to the previous and next pointers in a doubly-linked list.
# Let's take the following BST as an example, it may help you understand the problem better:

# We want to transform this BST into a circular doubly linked list. Each node in a doubly linked list has a predecessor and successor. 
# For a circular doubly linked list, the predecessor of the first element is the last element, and the successor of the last element is the first element.

# The figure below shows the circular doubly linked list for the BST above. 
# The "head" symbol means the node it points to is the smallest element of the linked list.
# Specifically, we want to do the transformation in place. After the transformation, 
# the left pointer of the tree node should point to its predecessor, and the right pointer should point to its successor. 
# We should return the pointer to the first element of the linked list.
# The figure below shows the transformed BST. The solid line indicates the successor relationship, 
# while the dashed line means the predecessor relationship.

# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        # 中序递归
        if not root:
            return None
        first, last = None, None

        def helper(node):
            # nonlocal only for python3
            # https://blog.csdn.net/youngbit007/article/details/64905070
            nonlocal first, last
            if node:
                # left
                helper(node.left)
                # node
                if last:
                    # link the previous node (last) with the current one (node)
                    last.right = node
                    node.left = last
                else:
                    # keep the smallest node to close DLL later on
                    first = node
                last = node
                # right
                helper(node.right)

        # process the middle nodes
        helper(root)

        # close Doubly Linked List
        last.right = first
        first.left = last

        return first