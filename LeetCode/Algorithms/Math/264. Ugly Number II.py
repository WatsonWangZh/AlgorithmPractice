# # Write a program to find the n-th ugly number.
# # Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

# # Example:
# # Input: n = 10
# # Output: 12
# # Explanation: 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.

# # Note:  
# # 1 is typically treated as an ugly number.
# # n does not exceed 1690.

# # Hints:
# The naive approach is to call isUgly for every number until you reach the nth one. 
# Most numbers are not ugly. Try to focus your effort on generating only the ugly ones.
# An ugly number must be multiplied by either 2, 3, or 5 from a smaller ugly number.
# The key is how to maintain the order of the ugly numbers. 
# Try a similar approach of merging from three sorted lists: L1, L2, and L3.
# Assume you have Uk, the kth ugly number. Then Uk+1 must be Min(L1 * 2, L2 * 3, L3 * 5).


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 三指针法
        # https://leetcode-cn.com/problems/ugly-number-ii/solution/san-zhi-zhen-fang-fa-de-li-jie-fang-shi-by-zzxn/
        
        ugly = [1]
        
        i2, i3, i5 = 0, 0, 0
        # i2, i3, i5 分别表示有资格同2，3，5相乘的最小丑数的位置，
        # 由于ugly数组添加时，只添加最小值，所以可以做到不重不漏。
        
        while(len(ugly) < n):
            
            while(ugly[i2] * 2 <= ugly[-1]):
                i2 +=1
                
            while(ugly[i3] * 3 <= ugly[-1]):
                i3 +=1
                
            while(ugly[i5] * 5 <= ugly[-1]):
                i5 +=1 
    
            ugly.append(min(ugly[i2] * 2, ugly[i3] * 3, ugly[i5] * 5))

        return ugly[-1]