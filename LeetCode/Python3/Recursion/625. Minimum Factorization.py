# Given a positive integer a, 
# find the smallest positive integer b whose multiplication of each digit equals to a.
# If there is no answer or the answer is not fit in 32-bit signed integer, then return 0.

# Example 1
# Input:
# 48 
# Output:
# 68

# Example 2
# Input:
# 15
# Output:
# 35

class Solution(object):
    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """

        # 蛮力算法 Memory Limit Exceeded
        # for i in range(1, 2**31):
        #     mul = 1
        #     tmp = i
        #     while tmp != 0:
        #         mul *= tmp % 10
        #         tmp /= 10
        #     if mul == a:
        #         return i
        # return 0

        # 贪心因式分解 O(logn) O(1)
        if a < 10:
            return a
        res = 0
        times = 1
        while a != 1:
            for d in range(9, 1, -1):
                if a % d == 0:
                    # print(res)
                    res += d * times
                    a /= d
                    times *= 10
                    break
            else:
                return 0
        return res if res < 2**31 else 0