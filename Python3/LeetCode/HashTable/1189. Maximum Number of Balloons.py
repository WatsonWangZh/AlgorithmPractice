# Given a string text,
#  you want to use the characters of text to form as many instances of the word "balloon" as possible.
# You can use each character in text at most once. 
# Return the maximum number of instances that can be formed.

# Example 1:
# Input: text = "nlaebolko"
# Output: 1

# Example 2:
# Input: text = "loonbalxballpoon"
# Output: 2

# Example 3:
# Input: text = "leetcode"
# Output: 0
 
# Constraints:
# 1 <= text.length <= 10^4
# text consists of lower case English letters only.

# Hints:
# Count the frequency of letters in the given string.
# Find the letter than can make the minimum number of instances of the word "balloon".

from collections import Counter
class Solution(object):
    def maxNumberOfBalloons(self, text):
        """
        :type text: str
        :rtype: int
        """
        # 计数看瓶颈 O(n)
        
        # dic = {}
        # for i in range(len(text)):
        #     if text[i] not in dic:
        #         dic[text[i]] = 1
        #     else:
        #         dic[text[i]] += 1
        # return min(dic.get('b',0), dic.get('a',0), dic.get('l',0)//2,
        #             dic.get('o',0)//2, dic.get('n',0))

        dic = Counter(text)
        return min(dic['b'], dic['a'], dic['l']//2, dic['o']//2, dic['n'])