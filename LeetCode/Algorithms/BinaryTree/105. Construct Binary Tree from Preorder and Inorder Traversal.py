# Given preorder and inorder traversal of a tree, construct the binary tree.
# Note:
# You may assume that duplicates do not exist in the tree.
# For example, given
# preorder = [3,9,20,15,7]
# inorder = [9,3,15,20,7]
# Return the following binary tree:
#     3
#    / \
#   9  20
#     /  \
#    15   7

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # preorder: root, left, right
    # inorder: left, root, right 
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # 递归 O(n)
        # 递归建立整棵二叉树：先递归创建左右子树，然后创建根节点，并让指针指向两棵子树。
        # 具体步骤如下：
        # 先利用前序遍历找根节点：前序遍历的第一个数，就是根节点的值；
        # 在中序遍历中找到根节点的位置 kk，则 kk 左边是左子树的中序遍历，右边是右子树的中序遍历；
        # 假设左子树的中序遍历的长度是 ll，则在前序遍历中，根节点后面的 ll 个数，是左子树的前序遍历，剩下的数是右子树的前序遍历；
        # 有了左右子树的前序遍历和中序遍历，我们可以先递归创建出左右子树，然后再创建根节点；
        
        if not preorder:
            return None

        val = preorder[0]
        root = TreeNode(val)
        idx = inorder.index(val)

        root.left = self.buildTree(preorder[1:1+idx], inorder[:idx])
        root.right = self.buildTree(preorder[1+idx:], inorder[idx+1:])
        return root
