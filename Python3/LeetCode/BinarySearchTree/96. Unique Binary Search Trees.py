# Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

# Example:
# Input: 3
# Output: 5
# Explanation:
# Given n = 3, there are a total of 5 unique BST's:
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 首先明确n个不等的数它们能构成的二叉搜索树的种类都是相等的。
        # 而且1到n都可以作为二叉搜索树的根节点，当k是根节点时，它的左边有k-1个不等的数，它的右边有n-k个不等的数。
        # 以k为根节点的二叉搜索树的种类就是左右可能的种类的乘积。
        # 用递推式表示就是 h(n) = h(0)*h(n-1) + h(1)*h(n-2) + ... + h(n-1)h(0) (其中n>=2) ，
        # 其中h(0)=h(1)=1，因为0个或者1个数能组成的形状都只有一个。从1到n依次算出h(x)的值即可。
        # 此外这其实就是一个卡特兰数，可以直接用数学公式计算，不过上面的方法更加直观一些。

        # M1. 无记忆搜索
        # dp = [0] * (n+1)
        # dp[0] = dp[1] = 1 

        # for i in range(2, n+1):
        #     for j in range(i):
        #         dp[i] += dp[j] * dp[i-j-1]

        # return dp[-1]

        # M2. 优化 记忆化搜索
        dp = [0] * (n+1)
        return self.helper(dp, n)

    def helper(self, dp, m):
            if m <= 1:
                return 1
            if dp[m] > 0:
                return dp[m]
            for i in range(m):
                left = self.helper(dp, i)
                right = self.helper(dp, m-i-1)
                dp[m] += left * right
            return dp[m]
