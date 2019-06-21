# Implement atoi which converts a string to an integer.
# The function first discards as many whitespace characters 
# as necessary until the first non-whitespace character is found. 
# Then, starting from this character, takes an optional initial 
# plus or minus sign followed by as many numerical digits as possible, 
# and interprets them as a numerical value.

# The string can contain additional characters after those 
# that form the integral number, which are ignored and 
# have no effect on the behavior of this function.
# If the first sequence of non-whitespace characters in str 
# is not a valid integral number, or if no such sequence exists 
# because either str is empty or it contains only whitespace characters, 
# no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.
# Note:
# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers 
# within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value 
# is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.

# Example 1:
# Input: "42"
# Output: 42

# Example 2:
# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.

# Example 3:
# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.

# Example 4:
# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.

# Example 5:
# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

class Solution(object):
    def myAtoi(self, str):
            """
            :type str: str
            :rtype: int
            """
            if len(str) == 0:
                return 0
            numDict = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}
            INT_MAX = 2**31-1
            INT_MIN = -2**31
            ans = 0
            i = 0
            
            while i < len(str) and str[i] == " ":
                i += 1
            
            sign = 1
            if i < len(str) and str[i] =="+":   
                i += 1
            elif i < len(str) and str[i] =="-":
                sign = -1
                i += 1
            
            while i < len(str):
                if str[i] > '9' or str[i] < '0':
                    break
                ans = ans*10+numDict[str[i]]
                if ans > INT_MAX:
                    break
                i += 1
            
            return max(INT_MIN,min(ans*sign,INT_MAX))

def main():
    s = Solution()
    print(s.myAtoi("42"))
    print(s.myAtoi("   -42"))
    print(s.myAtoi("4193 with words"))
    print(s.myAtoi("words and 987"))
    print(s.myAtoi("-91283472332"))


if __name__ == "__main__":
    main()