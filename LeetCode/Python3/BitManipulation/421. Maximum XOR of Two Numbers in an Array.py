# Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 2^31.
# Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.
# Could you do this in O(n) runtime?

# Example:
# Input: [3, 10, 5, 25, 2, 8]
# Output: 28

# Explanation: The maximum result is 5 ^ 25 = 28.

# M1. Bitwise Prefixes in HashSet
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum, mask = 0, 0
        for i in range(32)[::-1]:
            numMasked = set()
            mask |= (1 << i)
            for num in nums:
                numMasked.add(num & mask)
                
            tmp = maximum | (1 << i)
            for prefix in numMasked:
                if tmp ^ prefix in numMasked:
                    maximum = tmp
                    break

        return maximum

# M2. Trie树
class TrieNode():
    def __init__(self):
        self.children = [None, None]

class Solution:
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = TrieNode()
        for num in nums:
            tmp = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if not tmp.children[bit]:
                    tmp.children[bit] = TrieNode()
                tmp = tmp.children[bit]

        maximum = 0
        for num in nums:
            tmp, tmp_num = root, 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if tmp.children[1-bit]:
                    bit = 1 - bit
                tmp_num += bit << i
                tmp = tmp.children[bit]
            maximum = max(maximum, num^tmp_num)
        return maximum
