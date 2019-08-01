# Implement an iterator over a binary search tree (BST). 
# Your iterator will be initialized with the root node of a BST.
# Calling next() will return the next smallest number in the BST.
# Example:
#     7
#    / \
#   3   15
#      /  \
#     9   20
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false

# Note:
# next() and hasNext() should run in average O(1) time and uses O(h) memory, 
# where h is the height of the tree.
# You may assume that next() call will always be valid, that is, 
# there will be at least a next smallest number in the BST when next() is called.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BSTIterator(object):
    # 用栈来模拟BST的中序遍历过程，当前结点进栈，代表它的左子树正在被访问。
    # next求后继时，只需要弹出栈顶结点，取出它的值。然后将它的右儿子以及右儿子的左儿子等一系列结点进栈，
    # 这一步代表找右子树中的最左子结点，并记录路径上的所有结点。
    # hasNext判断是否还存在后继只需要判断栈是否为空即可，因为栈顶结点是下一次即将被访问到的结点。
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.stack = []
        node = root
        while node:
            self.stack.append(node)
            node = node.left
        

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        node = self.stack.pop()
        val = node.val
        node = node.right
        while node:
            self.stack.append(node)
            node = node.left
        return val
        

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
