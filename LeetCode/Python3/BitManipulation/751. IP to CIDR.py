# Given a start IP address ip and a number of ips we need to cover n, 
# return a representation of the range as a list (of smallest possible length) of CIDR blocks.
# A CIDR block is a string consisting of an IP, followed by a slash, and then the prefix length. 
# For example: "123.45.67.89/20". That prefix length "20" represents the number of common prefix bits in the specified range.

# Example 1:
# Input: ip = "255.0.0.7", n = 10
# Output: ["255.0.0.7/32","255.0.0.8/29","255.0.0.16/32"]

# Explanation:
# The initial ip address, when converted to binary, looks like this (spaces added for clarity):
# 255.0.0.7 -> 11111111 00000000 00000000 00000111
# The address "255.0.0.7/32" specifies all addresses with a common prefix of 32 bits to the given address,
# ie. just this one address.
# The address "255.0.0.8/29" specifies all addresses with a common prefix of 29 bits to the given address:
# 255.0.0.8 -> 11111111 00000000 00000000 00001000
# Addresses with common prefix of 29 bits are:
# 11111111 00000000 00000000 00001000
# 11111111 00000000 00000000 00001001
# 11111111 00000000 00000000 00001010
# 11111111 00000000 00000000 00001011
# 11111111 00000000 00000000 00001100
# 11111111 00000000 00000000 00001101
# 11111111 00000000 00000000 00001110
# 11111111 00000000 00000000 00001111
# The address "255.0.0.16/32" specifies all addresses with a common prefix of 32 bits to the given address,
# ie. just 11111111 00000000 00000000 00010000.
# In total, the answer specifies the range of 10 ips starting with the address 255.0.0.7 .
# There were other representations, such as:
# ["255.0.0.7/32","255.0.0.8/30", "255.0.0.12/30", "255.0.0.16/32"],
# but our answer was the shortest possible.
# Also note that a representation beginning with say, "255.0.0.7/30" would be incorrect,
# because it includes addresses like 255.0.0.4 = 11111111 00000000 00000000 00000100 
# that are outside the specified range.

# Note:
# ip will be a valid IPv4 address.
# Every implied address ip + x (for x < n) will be a valid IPv4 address.
# n will be an integer in the range [1, 1000].

# Hints:
# Convert the ip addresses to and from (long) integers. 
# You want to know what is the most addresses you can put in this block starting from the "start" ip, up to n. 
# It is the smallest between the lowest bit of start and the highest bit of n. Then, repeat this process with a new start and n.

class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        # 贪心找小于n的最大块 位运算。
        def ip2number(ip):
            arr = map(int, ip.split('.'))
            return arr[-1]+arr[-2]*256+arr[-3]*(256**2)+arr[-4]*(256**3)
        
        def number2ip(n):
            arr = [] 
            while n:
                d, n = n%256, n // 256
                arr.append(d)
            arr += (4-len(arr))*[0]
            return '.'.join(map(str, arr[::-1]))
        
        def first1pos(n):
            one = 1
            for i in range(0, 32):
                if n & (one << i):
                    return i
    
        res, num = [], ip2number(ip)
        while n:
            i = first1pos(num)
            while 2**i > n: 
                i -= 1
            res.append(number2ip(num)+'/'+str(32-i))
            n -= (2**i)
            num += (2**i)
        return res