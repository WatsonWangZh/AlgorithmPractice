# Design a data structure that supports all following operations in average O(1) time.
# insert(val): Inserts an item val to the set if not already present.
# remove(val): Removes an item val from the set if present.
# getRandom: Returns a random element from current set of elements. 
# Each element must have the same probability of being returned.

# Example:
# // Init an empty set.
# RandomizedSet randomSet = new RandomizedSet();
# // Inserts 1 to the set. Returns true as 1 was inserted successfully.
# randomSet.insert(1);
# // Returns false as 2 does not exist in the set.
# randomSet.remove(2);
# // Inserts 2 to the set, returns true. Set now contains [1,2].
# randomSet.insert(2);
# // getRandom should return either 1 or 2 randomly.
# randomSet.getRandom();
# // Removes 1 from the set, returns true. Set now contains [2].
# randomSet.remove(1);
# // 2 was already in the set, so return false.
# randomSet.insert(2);
# // Since 2 is the only number in the set, getRandom always return 2.
# randomSet.getRandom();

# M1. set强转list 不符合要求3，但可以通过
import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.d:
            self.d.add(val)
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.d:
            self.d.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        l = len(self.d)
        idx = random.randint(0, l-1)
        return list(self.d)[idx]

# M2. dict与list联合应用
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums, self.pos = list(), dict()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx] = last
            self.pos[last] = idx
            self.nums.pop()
            self.pos.pop(val)
            return True
        return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.nums) - 1)
        return self.nums[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()