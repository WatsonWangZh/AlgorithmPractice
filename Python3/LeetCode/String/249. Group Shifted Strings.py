# Given a string, we can "shift" each of its letter to its successive letter, for example: "abc" -> "bcd". 
# We can keep "shifting" which forms the sequence:
# "abc" -> "bcd" -> ... -> "xyz"
# Given a list of strings which contains only lowercase alphabets, group all strings that belong to the same shifting sequence.

# Example:
# Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
# Output: 
# [
#   ["abc","bcd","xyz"],
#   ["az","ba"],
#   ["acef"],
#   ["a","z"]
# ]

class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        
        # https://leetcode.com/problems/group-shifted-strings/discuss/282285/Python-Solution-with-Explanation-(44ms-84)
        # We can solve this problem by mapping each string in strings to a key in a hashmap. We then return hashmap.values().
        # {
        #      (1, 1): ['abc', 'bcd', 'xyz'],  
        #   (2, 2, 1): ['acef'],   
        #       (25,): ['az', 'ba'],   
        #          (): ['a', 'z']
        # }
        # The key can be represented as a tuple of the "differences" between adjacent characters. 
        # Characters map to integers (e.g. ord('a') = 97). 
        # For example, 'abc' maps to (1,1) because ord('b') - ord('a') = 1 and ord('c') - ord('b') = 1
        # We need to watch out for the "wraparound" case - 
        # for example, 'az' and 'ba' should map to the same "shift group" as a + 1 = b and z + 1 = a. 
        # Given the above point, the respective tuples would be (25,) (122 - 97) and (-1,) (79 - 80) 
        # and az and ba would map to different groups. This is incorrect.
        # To account for this case, we add 26 to the difference between 
        # letters (smallest difference possible is -25, za) and mod by 26. So, (26 + 122 - 97) % 26 
        # and (26 + 79 - 80) % 26 both equal (25,)

        # Time complexity would be O(ab) where a is the total number of strings 
        # and b is the length of the longest string in strings.
        # Space complexity would be O(n), as the most space 
        # we would use is the space required for strings and the keys of our hashmap.

        hashmap = {}
        for s in strings:
            key = ()
            for i in range(len(s) - 1):
                circular_difference = 26 + ord(s[i+1]) - ord(s[i])
                key += (circular_difference % 26,)
            hashmap[key] = hashmap.get(key, []) + [s]
        return list(hashmap.values())
        