# Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. 
# Find and return the shortest palindrome you can find by performing this transformation.

# Example 1:
# Input: "aacecaaa"
# Output: "aaacecaaa"

# Example 2:
# Input: "abcd"
# Output: "dcbabcd"

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        # M1. 基本想法 最长前缀匹配
        t = s[::-1]
        for i in range(len(t) + 1):
            if s.startswith(t[i:]):
                return t[:i] + s

        # M2. KMP优化算法
        # 思路：
        # 我们知道，对于任意的字符串，不管它是不是回文串，我们将其翻转在添加到原串上，它一定是回文串。
        # 比如题目中的
            # aacecaaa => aaacecaaaacecaaa
            # abcd => dcbaabcd
        # OK, 但是这样会有很多没必要的字符在里面。比如dcbaabcd中间冗余了一个a，我们需要去掉它，才能变为最短的回文串。
        # 怎么去掉呢？其实去掉的过程就是求原串s的前缀在其逆序的revs中最长能匹配的后缀长度。
        # 这里用到了KMP里的失配函数。
        # KMP的失配函数f[i]表示为当前字符应该去与哪个数比较。
        # 如果我们将s翻转为revs，然后将s链接上revs（为了避免两个串混起来，在中间加上了’#’也就是 s + ‘#’ + revs），
        # 然后求失配函数。这样，就可以求出前缀在后缀中匹配了多少个字符！而剩下不匹配的就是我们要添加的字符啦。
        # 比如，
            # 题目中的aacecaaa 变为了 aacecaaa#aaacecaa 它的失配函数值为：
            # [0, 0, 1, 0, 0, 0, 1, 2, 2, 0, 1, 2, 2, 3, 4, 5, 6, 7]
            # 也就是说，最后前后缀匹配了7个(已经加粗)，我们只需要添加1个字符进去就可以了。 这个字符就是revs的第一个字符
        # 再比如，题目中的abcd变为了abcd#dcba, 失配函数值为：
            # [0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
            # 最后前后缀只匹配了1个数(已经加粗)，说明我们需要添加3个数进去。
        # 图解 KMP算法: https://blog.csdn.net/liu88010988/article/details/50789960

        m = len(s)
        P = s + '#' + s[::-1]
        n = len(P)
        # KMP
        f = [0] * (n + 1)
        for i in range(1, n):
            j = f[i]
            while j > 0 and P[j] != P[i]:
                j = f[j]
            f[i + 1] = j + 1 if P[j] == P[i] else 0
        return s[::-1][:m - f[n]] + s
