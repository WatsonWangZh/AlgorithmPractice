# There are N children standing in a line. Each child is assigned a rating value.
# You are giving candies to these children subjected to the following requirements:
# Each child must have at least one candy.
# Children with a higher rating get more candies than their neighbors.
# What is the minimum candies you must give?

# Example 1:
# Input: [1,0,2]
# Output: 5
# Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

# Example 2:
# Input: [1,2,2]
# Output: 4
# Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
#              The third child gets 1 candy because it satisfies the above two conditions.

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # M1. 蛮力 TLE
        n = len(ratings)
        candies = [1 for _ in range(n)]
        flag = True
        res = 0
        while flag:
            flag = False
            for i in range(n):
                if i != n-1 and ratings[i] > ratings[i+1] and candies[i] <= candies[i+1]:
                    candies[i] = candies[i+1] + 1
                    flag = True
                if i > 0 and ratings[i] > ratings[i-1] and candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1] + 1
                    flag = True
        for candy in candies:
            res += candy
        return res

        # M2. 找规律 双数组
        n = len(ratings)
        left2right = [1 for _ in range(n)]
        right2left = [1 for _ in range(n)]
        res = 0
        
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                left2right[i] = left2right[i-1] + 1
                
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                right2left[i] = right2left[i+1] + 1
        
        for i in range(n):
            res += left2right[i] if left2right[i] > right2left[i] else right2left[i]
        
        return res

        # M3. 找规律 单数组
        n = len(ratings)
        candies = [1 for _ in range(n)]

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
            
        return sum(candies)