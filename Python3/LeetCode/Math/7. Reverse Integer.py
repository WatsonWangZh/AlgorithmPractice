# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:
# Input: 123
# Output: 321

# Example 2:
# Input: -123
# Output: -321

# Example 3:
# Input: 120
# Output: 21

# Note:
# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. 
# For the purpose of this problem, assume that your function returns 0 
# when the reversed integer overflows.

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """      
        # Dirty Method 
        
        # if x > 0:
        #     x = str(x)
        #     x = x[::-1]
        #     x = int(x)
        # else :
        #     x = -x
        #     x = str(x)
        #     x = x[::-1]
        #     x = -int(x)
        # if x >= -2**31 and x<= 2**31-1:
        #     return x
        # else :
        #     return 0

        maxInt , minInt = 2**31-1,-1*2**31
        if x < 0:
            y = -1 * int (str(-x)[::-1])
        else:
            y = int(str(x)[::-1])
        if y > maxInt or y < minInt:
            return 0
        else:
            return y

def main():
    s = Solution()
    print(s.reverse(123))
    print(s.reverse(-123))
    print(s.reverse(120))

if __name__ == "__main__":
    main()