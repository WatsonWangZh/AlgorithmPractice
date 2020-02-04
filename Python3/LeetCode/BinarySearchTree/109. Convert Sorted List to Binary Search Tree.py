# Given a singly linked list where elements are sorted in ascending order, 
# convert it to a height balanced BST.
# For this problem, a height-balanced binary tree is defined as a binary tree 
# in which the depth of the two subtrees of every node never differ by more than 1.

# Example:
# Given the sorted linked list: [-10,-3,0,5,9],
# One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#       0
#      / \
#    -3   9
#    /   /
#  -10  5

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # M1. 存储为数组 采用108题解法
        lst = []
        while head:
            lst.append(head.val)
            head = head.next

        def sortedArrayToBST(arr):
            if not arr:
                return None
            length = len(arr)
            root = TreeNode(arr[length//2])
            root.left = sortedArrayToBST(arr[:length//2])
            root.right = sortedArrayToBST(arr[length//2+1:])
            return root
        return sortedArrayToBST(lst)
        
        # M2. 快慢指针法找链表中点
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        
        def findMid(head):
            fast, slow = head, head
            prev = None
            while fast and fast.next:
                fast = fast.next.next
                prev = slow
                slow = slow.next
            prev.next = None
            return slow
        
        mid = findMid(head)
        root = TreeNode(mid.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(mid.next)
        return root