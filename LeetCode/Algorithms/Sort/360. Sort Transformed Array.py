# Given a sorted array of integers nums and integer values a, b and c. 
# Apply a quadratic function of the form f(x) = ax^2 + bx + c to each element x in the array.
# The returned array must be in sorted order.
# Expected time complexity: O(n)

# Example 1:
# Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
# Output: [3,9,15,33]

# Example 2:
# Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
# Output: [-23,-5,1,7]

# Hints:
# x^2 + x will form a parabola.
# Parameter A in: A * x^2 + B * x + C dictates the shape of the parabola.
# Positive A means the parabola remains concave (high-low-high), 
# but negative A inverts the parabola to be convex (low-high-low).

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """
        # M1. One Line Solution O(nlgn)
        # return sorted(a*x**2 + b*x + c for x in nums)

        # M2. 双指针填充 Hints Solution

        def quadratic(num, a, b, c):
            return a*num**2 + b*num + c
    
        n = len(nums)
        i = 0
        j = n-1
        res = [0 for _ in range(n)]

        # 根据a的正负确定正向填充还是逆向填充
        idx = 0 if a < 0 else n-1 

        # a >= 0 means two ends of array is large, a < 0 means two ends of array is small
        # when a == 0, we still need to find the big one and put it to the end of ans
        while i <= j:
            num1 = quadratic(nums[i], a, b, c)
            num2 = quadratic(nums[j], a, b, c)
            if a >= 0: # which end is large?
                if num1 > num2:
                    res[idx] = num1
                    i += 1
                else:
                    res[idx] = num2
                    j -= 1
                idx -= 1
            else: # which end is small?
                if num1 > num2:
                    res[idx] = num2
                    j -= 1
                else:
                    res[idx] = num1
                    i += 1
                idx += 1

        return res