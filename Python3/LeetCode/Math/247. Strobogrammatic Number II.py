# A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
# Find all strobogrammatic numbers that are of length = n.

# Example:
# Input:  n = 2
# Output: ["11","69","88","96"]

# Hints:
# Try to use recursion and notice that it should recurse with n - 2 instead of n - 1.

class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        # M1. 递归解法
        # n = 0:   none
        # n = 1:   0, 1, 8
        # n = 2:   11, 69, 88, 96
        # n = 3:   101, 609, 808, 906, 111, 619, 818, 916, 181, 689, 888, 986
        # n = 4:   1001, 6009, 8008, 9006, 1111, 6119, 8118, 9116, 1691, 6699, 8698, 9696, 1881, 6889, 8888, 9886, 1961, 6969, 8968, 9966
        # 我们注意观察n=0和n=2，可以发现后者是在前者的基础上，每个数字的左右增加了[1 1], [6 9], [8 8], [9 6]，
        # 看n=1和n=3更加明显，在0的左右增加[1 1]，变成了101, 在0的左右增加[6 9]，变成了609, 
        # 在0的左右增加[8 8]，变成了808, 在0的左右增加[9 6]，变成了906, 
        # 然后在分别在1和8的左右两边加那四组数，我们实际上是从m=0层开始，一层一层往上加的，
        # 需要注意的是当加到了n层的时候，左右两边不能加[0 0]，因为0不能出现在两位数及多位数的开头，
        # 在中间递归的过程中，需要有在数字左右两边各加上0的情况。

        # def processString(arr, n, total):
        #     res = []
        #     for s in arr:
        #         if n != total:
        #             res.append('0' + s + '0')
        #         res.append('1' + s + '1')
        #         res.append('8' + s + '8')
        #         res.append('6' + s + '9')
        #         res.append('9' + s + '6')
        #     return res 
        
        # def findImp(n,total):
        #     # base cases
        #     if n == 0:
        #         return [""]
        #     if n == 1:
        #         return ["0","1","8"]
        #     return processString(findImp(n-2, total), n, total)
        
        # return findImp(n,n)

        # M2. 迭代解法
        # 从奇偶来考虑，奇数赋为0,1,8，偶数赋为空，
        # 如果是奇数，就从i=3开始搭建，因为计算i=3需要i=1，而我们已经初始化了i=1的情况，
        # 如果是偶数，我们从i=2开始搭建，我们也已经初始化了i=0的情况，
        # 所以我们可以用for循环来搭建到i=n的情况，思路和递归一样，写法不同而已。

        odd_Num = ["0", "1", "8"]
        even_Num = [""]

        result = even_Num

        if n % 2 == 1:
            result = odd_Num

        for i in range((n%2)+2, n+1, 2):
            temp = []
            for ele in result:
                if i != n: 
                    temp.append("0" + ele + "0")
                temp.append("1" + ele + "1")
                temp.append("6" + ele + "9")
                temp.append("8" + ele + "8")
                temp.append("9" + ele + "6")
            result = temp

        return result
