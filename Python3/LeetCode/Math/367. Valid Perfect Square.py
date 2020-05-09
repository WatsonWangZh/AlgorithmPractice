# Given a positive integer num, 
# write a function which returns True if num is a perfect square else False.

# Note: Do not use any built-in library function such as sqrt.

# Example 1:
# Input: 16
# Output: true

# Example 2:
# Input: 14
# Output: false

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 蛮力 O(n^1/2)
        i = 1
        while i*i < num:
            tmp = i*i
            if tmp == num:
                return True
            i += 1
        return False

        # 折半
        if num < 2:
            return True
        
        left, right = 2, num // 2
        
        while left <= right:
            x = left + (right - left) // 2
            guess_squared = x * x
            if guess_squared == num:
                return True
            if guess_squared > num:
                right = x - 1
            else:
                left = x + 1
        
        return False

