# Given a binary tree, return all root-to-leaf paths.
# Note: A leaf is a node with no children.
# Example:
# Input:
#    1
#  /   \
# 2     3
#  \
#   5
# Output: ["1->2->5", "1->3"]
# Explanation: All root-to-leaf paths are: 1->2->5, 1->3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        # DFS 
        if not root:
            return []
        res = []
        self.dfs(root, '', res)
        return res

    def dfs(self, root, curr, paths):
        if not root.left and not root.right:
            paths.append(curr+str(root.val))
        if root.left:
            self.dfs(root.left, curr+str(root.val)+'->', paths)
        if root.right:
            self.dfs(root.right, curr+str(root.val)+'->', paths)
        
        # 递归
        # def construct_paths(root, path):
        #     if root:
        #         path += str(root.val)
        #         if not root.left and not root.right:  # if reach a leaf
        #             paths.append(path)  # update paths  
        #         else:
        #             path += '->'  # extend the current path
        #             construct_paths(root.left, path)
        #             construct_paths(root.right, path)

        # paths = []
        # construct_paths(root, '')
        # return paths

        # # 迭代
        # if not root:
        #     return []
        
        # paths = []
        # stack = [(root, str(root.val))]
        # while stack:
        #     node, path = stack.pop()
        #     if not node.left and not node.right:
        #         paths.append(path)
        #     if node.left:
        #         stack.append((node.left, path + '->' + str(node.left.val)))
        #     if node.right:
        #         stack.append((node.right, path + '->' + str(node.right.val)))
        
        # return paths
