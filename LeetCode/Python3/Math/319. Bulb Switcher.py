# There are n bulbs that are initially off. 
# You first turn on all the bulbs. 
# Then, you turn off every second bulb. 
# On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
# For the i-th round, you toggle every i bulb. 
# For the n-th round, you only toggle the last bulb. 
# Find how many bulbs are on after n rounds.

# Example:
# Input: 3
# Output: 1 
# Explanation: 
# At first, the three bulbs are [off, off, off].
# After first round, the three bulbs are [on, on, on].
# After second round, the three bulbs are [on, off, on].
# After third round, the three bulbs are [on, off, off]. 
# So you should return 1, because there is only one bulb is on.

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 数论 O(1)
        # 每个灯泡开关被按的次数等于它的编号的约数个数。
        # 最终灯泡是亮的，说明编号有奇数个约数。
        # 一个数有奇数个约数，等价于它是平方数。

        return int(n**0.5)
