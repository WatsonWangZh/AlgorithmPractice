# Determine whether an integer is a palindrome. 
# An integer is a palindrome when it reads the same backward as forward.

# Example 1:
# Input: 121
# Output: true

# Example 2:
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
# Therefore it is not a palindrome.

# Example 3:
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# Follow up:
# Coud you solve it without converting the integer to a string?

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # return x >= 0 and x == int(str(x)[::-1])
        
        # a = str(x)
        # if a == a[::-1]:
        #     return True
        # else:
        #     return False
        
        if x < 0:
            return False
        if x == 0:
            return True
        if x % 10 == 0 :
            return False
        
        y = 0
        while(x>y):
            y = y * 10 + x % 10
            x = x/10
        return y == x or (y > x and y/10 == x)

def main():
    s = Solution()
    print(s.isPalindrome(121))
    print(s.isPalindrome(-121))
    print(s.isPalindrome(10))

if __name__ == "__main__":
    main()