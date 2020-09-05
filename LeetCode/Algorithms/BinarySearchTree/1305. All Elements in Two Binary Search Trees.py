# Given two binary search trees root1 and root2.
# Return a list containing all the integers from both trees sorted in ascending order.

# Example 1:
# Input: root1 = [2,1,4], root2 = [1,0,3]
# Output: [0,1,1,2,3,4]

# Example 2:
# Input: root1 = [0,-10,10], root2 = [5,1,7,0,2]
# Output: [-10,0,0,1,2,5,7,10]

# Example 3:
# Input: root1 = [], root2 = [5,1,7,0,2]
# Output: [0,1,2,5,7]

# Example 4:
# Input: root1 = [0,-10,10], root2 = []
# Output: [-10,0,10]

# Example 5:
# Input: root1 = [1,null,8], root2 = [8,1]
# Output: [1,1,8,8]
 
# Constraints:
# Each tree has at most 5000 nodes.
# Each node's value is between [-10^5, 10^5].

# Hints:
# Traverse the first tree in list1 and the second tree in list2.
# Merge the two trees in one list and sort it.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        # 中序遍历 + 归并排序
        def dfs(node, v):
            if not node:
                return
            dfs(node.left, v)
            v.append(node.val)
            dfs(node.right, v)
        
        v1, v2 = [], []
        dfs(root1, v1)
        dfs(root2, v2)
        res, i, j = [], 0, 0
        while i < len(v1) or j < len(v2):
            if i < len(v1) and (j == len(v2) or v1[i] <= v2[j]):
                res.append(v1[i])
                i += 1
            else:
                res.append(v2[j])
                j += 1
        return res
