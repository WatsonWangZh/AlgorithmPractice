# Given a non negative integer number num. 
# For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation 
# and return them as an array.

# Example 1:
# Input: 2
# Output: [0,1,1]

# Example 2:
# Input: 5
# Output: [0,1,1,2,1,2]

# Follow up:
# It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
# But can you do it in linear time O(n) /possibly in a single pass?
# Space complexity should be O(n).
# Can you do it like a boss? 
# Do it without using any builtin function like __builtin_popcount in c++ or in any other language.

class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        
        # M1. 内置函数
        # return [bin(i).count('1') for i in range(num+1)]

        # M2. DP O(n)
        # 假设n为100…，则n-1为00..1，n&(n-1)=0。说明n&(n-1)消去了末尾的1

        # result = [0]
        # for i in range(1, num+1):
        #     result.append(result[i & (i-1)] + 1)
        # return result

        # M3. DP O(n)
        # 令dp[i]表示 i 的二进制表示中1的个数。
        # 则dp[i]可以由dp[i/2]转移过来，i 的二进制表示和 ⌊i/2⌋ 的二进制表示除了最后一位都一样，所以dp[i] = dp[i/2] + (i&1);
        # # 时间复杂度分析：
        # 总共有 n 个状态，每个状态进行转移的计算量是 O(1)，所以总时间复杂度是 O(n)。

        dp = [0]
        for i in range(1, num+1):
            dp.append(dp[i>>1] + (i&1))
        return dp
