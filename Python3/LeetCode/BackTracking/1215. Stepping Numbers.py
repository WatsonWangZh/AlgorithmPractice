# A Stepping Number is an integer such that 
# all of its adjacent digits have an absolute difference of exactly 1. 
# For example, 321 is a Stepping Number while 421 is not.
# Given two integers low and high, 
# find and return a sorted list of all the Stepping Numbers in the range [low, high] inclusive.

# Example 1:
# Input: low = 0, high = 21
# Output: [0,1,2,3,4,5,6,7,8,9,10,12,21]
 
# Constraints:
# 0 <= low <= high <= 2 * 10^9

# Hints:
# Try to generate the numbers using recursion.
# In one step in the recursion, add a valid digit to the right of the current number.
# Save the number if it's in the range between low and high.

class Solution(object):
    def countSteppingNumbers(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """
        # https://www.geeksforgeeks.org/stepping-numbers/
        
        # M1. 模拟遍历 Memory Exceeded
        res = []
        for i in range(low, high+1):
            if self.isStepNum(i):
                res.append(i)
        return res
        
    def isStepNum(self, num):
        prevDigit = -1 
        # Iterate through all digits of n and compare difference between value of previous and current digits 
        while num:
            # Get Current digit 
            curDigit = num % 10
            # Single digit is consider as a Stepping Number 
            if prevDigit == -1:
                prevDigit = curDigit
            else:
                # Check if absolute difference between prev digit and current digit is 1 
                if abs(prevDigit - curDigit) != 1:
                     return False
            prevDigit = curDigit
            num /= 10
        return True 

        # M2. 规律 DFS
        res = []
        for i in range(10):    
            self.dfs(low, high, i, res)
        return sorted(res)

    def dfs(self, low, high, stepNum, res):
        # If Stepping Number is in the range [n,m] then append to res
        if stepNum <= high and stepNum >= low:
            res.append(stepNum)

        # If Stepping Number is 0 or greater than m, then return 
        if stepNum == 0 or stepNum > high:
            return 

        # Get the last digit of the currently visited Stepping Number 
        lastDigit = stepNum % 10
        # There can be 2 cases either digit to be appended is lastDigit + 1 or lastDigit - 1 
        stepNumA = stepNum*10 + (lastDigit-1)
        stepNumB = stepNum*10 + (lastDigit+1) 

        # If lastDigit is 0 then only possible digit after 0 can be 1 for a Stepping Number 
        if lastDigit == 0:
            self.dfs(low, high, stepNumB, res)
 
        # If lastDigit is 9 then only possible digit after 9 can be 8 for a Stepping Number 
        elif lastDigit == 9:
            self.dfs(low, high, stepNumA, res)
        else:
            self.dfs(low, high, stepNumA, res)
            self.dfs(low, high, stepNumB, res)

        
        # M3. 规律 BFS
        res = []
        for i in range(10):    
            self.bfs(low, high, i, res)
        return sorted(res)

    def bfs(self, low, high, num, res):
        q = []
        q.append(num)
        while q: 
            # Get the front element and pop from the queue 
            stepNum = q.pop() 
    
            # If the Stepping Number is in the range [n, m] then append to res 
            if stepNum <= high and stepNum >= low:
                res.append(stepNum)
    
            # If Stepping Number is 0 or greater than m, need to explore the neighbors 
            if num == 0 or stepNum > high: 
                continue
    
            # Get the last digit of the currently visited Stepping Number 
            lastDigit = stepNum % 10
    
            # There can be 2 cases either digit to be appended is lastDigit + 1 or lastDigit - 1 
            stepNumA = stepNum * 10 + (lastDigit- 1)
            stepNumB = stepNum * 10 + (lastDigit + 1)
    
            # If lastDigit is 0 then only possible digit after 0 can be 1 for a Stepping Number 
            if lastDigit == 0:
                q.append(stepNumB) 
    
            # If lastDigit is 9 then only possible digit after 9 can be 8 for a Stepping Number 
            elif lastDigit == 9:
                q.append(stepNumA) 
            else:
                q.append(stepNumA) 
                q.append(stepNumB)