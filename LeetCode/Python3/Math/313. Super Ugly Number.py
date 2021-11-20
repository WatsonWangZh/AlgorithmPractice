# Write a program to find the nth super ugly number.
# Super ugly numbers are positive numbers 
# whose all prime factors are in the given prime list primes of size k.

# Example:
# Input: n = 12, primes = [2,7,13,19]
# Output: 32 
# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
#              super ugly numbers given primes = [2,7,13,19] of size 4.

# Note:
# 1 is a super ugly number for any given primes.
# The given numbers in primes are in ascending order.
# 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
# The nth super ugly number is guaranteed to fit in a 32-bit signed integer.

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:

        ugly = []
        ugly.append(1)
        
        idx = [0 for _ in range(len(primes))]
        
        while len(ugly) < n:
            tmp = []
            mn = float('inf')
            
            for i in range(len(primes)):
                tmp.append(ugly[idx[i]] * primes[i])
            # print(tmp)
            mn = min(tmp)
            
            for i in range(len(primes)):
                if tmp[i] == mn:
                    idx[i] += 1
                    
            ugly.append(mn)    
            # print(ugly, idx)
        return ugly[-1]