# You have some apples, where arr[i] is the weight of the i-th apple.  
# You also have a basket that can carry up to 5000 units of weight.
# Return the maximum number of apples you can put in the basket.

# Example 1:
# Input: arr = [100,200,150,1000]
# Output: 4
# Explanation: All 4 apples can be carried by the basket since their sum of weights is 1450.

# Example 2:
# Input: arr = [900,950,800,1000,700,800]
# Output: 5
# Explanation: The sum of weights of the 6 apples exceeds 5000 so we choose any 5 of them.

# Hints:
# What if you think in a greedy approach?
# The best apple to take in one step is the one with the smallest weight.
# Sort the array and take apples with smaller weight first.

class Solution(object):
    def maxNumberOfApples(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        arr.sort()
        temp_sum = cnt = 0
        for num in arr:
            if temp_sum + num <= 5000:
                temp_sum += num
                cnt += 1
            else:
                break
        return cnt