# At a lemonade stand, each lemonade costs $5. 
# Customers are standing in a queue to buy from you, 
# and order one at a time (in the order specified by bills).
# Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.  
# You must provide the correct change to each customer, 
# so that the net transaction is that the customer pays $5.
# Note that you don't have any change in hand at first.
# Return true if and only if you can provide every customer with correct change.

# Example 1:
# Input: [5,5,5,10,20]
# Output: true
# Explanation: 
# From the first 3 customers, we collect three $5 bills in order.
# From the fourth customer, we collect a $10 bill and give back a $5.
# From the fifth customer, we give a $10 bill and a $5 bill.
# Since all customers got correct change, we output true.

# Example 2:
# Input: [5,5,10]
# Output: true

# Example 3:
# Input: [10,10]
# Output: false

# Example 4:
# Input: [5,5,10,10,20]
# Output: false
# Explanation: 
# From the first two customers in order, we collect two $5 bills.
# For the next two customers in order, we collect a $10 bill and give back a $5 bill.
# For the last customer, we can't give change of $15 back because we only have two $10 bills.
# Since not every customer received correct change, the answer is false.
 
# Note:
# 0 <= bills.length <= 10000
# bills[i] will be either 5, 10, or 20.

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        # 贪心 O(n)
        # 开两个变量记录手中 5 元和 10 元的数量。
        # 收到 5 元，直接增加一张 5 元；
        # 收到 10 元，如果没有 5 元了，则返回 false；
        # 收到 20 元，则如果有 10 元的，并且也有至少一张 5 元的，
        # 则优先将 10 元配 5 元纸币的找回（因为 5 元的可以更灵活）；
        # 如果没有 10 元的，但 5 元的有三张，则直接找回三张 5 元的。
        # 否则，无法找零，返回 false。
        # 时间复杂度
        # 只需遍历一次数组，故时间复杂度为 O(n)。
        # 空间复杂度
        # 只需要常数个额外的变量，故空间复杂度为 O(1)。

        n5 = 0
        n10 = 0
        for b in bills:
            if b==5:
                n5 += 1
            elif b==10:
                if n5:
                    n5 -= 1
                    n10 += 1
                else:
                    return False
            elif b==20:
                if n5 and n10:
                    n5 -= 1
                    n10 -= 1
                elif n5>=3:
                    n5 -= 3
                else:
                    return False
        return True
