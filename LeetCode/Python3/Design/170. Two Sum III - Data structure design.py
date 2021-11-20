# Design and implement a TwoSum class. It should support the following operations: add and find.
# add - Add the number to an internal data structure.
# find - Find if there exists any pair of numbers which sum is equal to the value.

# Example 1:
# add(1); add(3); add(5);
# find(4) -> true
# find(7) -> false

# Example 2:
# add(3); add(1); add(2);
# find(3) -> true
# find(6) -> false

class TwoSum(object):
    
    # 哈希表 add:O(1) find:O(n)
    # 用哈希表统计每个数的个数。
    # add(x) - 直接将 x 插入哈希表；
    # find(target) - 枚举集合中的每个数 x，判断与 x 互补的数 target−x 是否也在集合中。
    # 这里要注意每个数只能使用一次，所以如果恰好 2x=target 时，集合中需要至少存在2个 x 才可以凑出 target。
    # 时间复杂度分析：
    # add操作仅有一次哈希表的插入操作，时间复杂度是 O(1)，
    # find 需要枚举集合中的每个数，时间复杂度是 O(n)。

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = {}

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: None
        """
        if number in self.nums:
            self.nums[number] += 1
        else:
            self.nums[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        for num in self.nums:
            if value - num in self.nums:
                if value - num != num:
                    return True
                elif value - num == num and self.nums[num] > 1:
                    return True
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)