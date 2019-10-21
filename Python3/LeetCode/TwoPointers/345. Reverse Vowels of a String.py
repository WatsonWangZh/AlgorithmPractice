# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:
# Input: "hello"
# Output: "holle"

# Example 2:
# Input: "leetcode"
# Output: "leotcede"

# Note:
# The vowels does not include the letter "y".

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        # M1. 两端双指针 增加过滤操作 
        # 时: O(n) 空: O(1)
        # vowels = set(list("aeiouAEIOU"))
        # s = list(s)
        # l, r = 0, len(s) - 1
        # while l < r:
        #     while s[l] not in vowels and l < r:
        #         l += 1
        #     while s[r] not in vowels and l < r:
        #         r -= 1
            
        #     tmp = s[r]
        #     s[r] = s[l]
        #     s[l] = tmp
        #     l += 1
        #     r -= 1
        # return "".join(s)

        # M2. 先遍历记录需替换元素位置及值，然后逆序替换
        # 时: O(n) 空: O(n)
        position = []
        characters = []
        vowels = set(list("aeiouAEIOU"))
        s = list(s)
        for i, c in enumerate(s):
            if c in vowels:
                position.append(i)
                characters.append(c)
                
        characters = characters[::-1]
        for i in range(len(position)):
            s[position[i]] = characters[i]
            
        return ''.join(s)