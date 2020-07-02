# n passengers board an airplane with exactly n seats. 
# The first passenger has lost the ticket and picks a seat randomly. 
# But after that, the rest of passengers will:
# Take their own seat if it is still available, 
# Pick other seats randomly when they find their seat occupied 
# What is the probability that the n-th person can get his own seat?

# Example 1:
# Input: n = 1
# Output: 1.00000
# Explanation: The first person can only get the first seat.

# Example 2:
# Input: n = 2
# Output: 0.50000
# Explanation: The second person has a probability of 0.5 to get the second seat (when first person gets the first seat).
 
# Constraints:
# 1 <= n <= 10^5

# Hints:
# Use dynamic programming, dp[i] indicates the probability that the i-th person can get his seat when there're i persons in total. 
# It's okay to start with O(n^2) solution and then optimize it.
# Try to find the regular pattern of the result.

class Solution(object):
    def nthPersonGetsNthSeat(self, n):
        """
        :type n: int
        :rtype: float
        """
        # M1. DP推导 O(n) O(n)
        # https://leetcode.com/problems/airplane-seat-assignment-probability/discuss/407533/Python-from-O(n)-to-O(1)-with-detailed-explanation
        # Each round we have 3 choices:
        # the 1st person gets his/her own seat. (with probability 1/n). Then the n-th person is sure (with probability 1) to get the n-th seat.
        # the 1st person gets the n-th person's seat. (with probability 1/n). Then the n-th person cannot (with probability 0) get the n-th seat.
        # the 1st person gets a seat between 2 and n-1 (with probability (n-2)/n). Assume the 1st person gets a-th seat. 
        # Then in the next round, we have 3 choices again:
            # 3.1) if the a-th person gets 1st seat (with probability 1/(n-1)), then this is just like 1st and a-th person swap their seats, 
            # it never affect our result for the n-th person.
            # 3.2) if the a-th person gets n-th seat (with probability 1/(n-1)), game over.
            # 3.3) if the a-th person gets a seat which is not 1st or n-th, (with probability (n-1-2)/(n-1)), we jump into a loop.
        # Therefore the dp pattern is dp[i] = 1.0 / (i+1) + 0.0 / (i+1) + dp[i-1] * (i-1) / (i+1), with dp[0]=1 for the case there's only one person. 
        # If you manually calculate it you'll find dp[i] is always 1/2 except the base condition.

        # dp = [0] * (n+1)
        # dp[1] = 1.
        # for i in range(2, n+1):
        #     dp[i] = 1.0 / i + dp[i-1] * (i-2) / i
        # return dp[-1]

        # M2. 数学推导 O(1)
        # Prove the probability is 0.5 with n >= 2
        # https://leetcode.com/problems/airplane-seat-assignment-probability/discuss/408405/Prove-the-probability-is-0.5-with-n-greater-2
        # Define dp[n] is the probability with passenger n can seat on seat n.
        # Then first person has three kinds choices:
        # 1.chose the correct seat, which is seat 1, then passenger n defintely seat on seat n;
        # 2.chose the nth seat, then passenger n can never seat on seat n;
        # 3.chose the kth seat, where 2<=k<= n - 1, then passengers 2 to k - 1 will seat their seats, so we have a sub-problem which size is n - (k - 1)
        # So the dp[n] = 1/n + ∑(1/n * dp[n - (k - 1)]) where k between 2 and n - 1, 
        # which also can expressed as dp[n] = 1/n + ∑(1/n * dp[n - k + 1]) where k between 2 and n - 1

        # Then we can prove dp[n] = dp[n + 1] if n > 2
        # dp[n] = 1/n + ∑(1/n * dp[n - k + 1])  where 2<=k<= n -1
        # => n * dp[n] = 1 + dp[2] + dp[3] + ... + dp[n - 1]
        #    dp[n + 1] = 1/(n + 1) + ∑(1/(n + 1) * dp[(n + 1) - k + 1]) where 2<=k<= n
        # => dp[n + 1] = 1/(n + 1) + 1/(n + 1) * (dp[2] + dp[3] + ... dp[n - 1] + dp[n])
        # => dp[n + 1] = 1/(n + 1) * (1 + dp[2] + dp[3] + ... dp[n - 1] + dp[n])
        # => dp[n + 1] = 1/(n + 1) * (n * dp[n] + dp[n])
        # => dp[n + 1] = dp[n]
        # It is easy to find dp[2] = dp[3] = 0.5, then for any n >= 2, dp[n] = 0.5

        return 0.5 if n > 1 else 1