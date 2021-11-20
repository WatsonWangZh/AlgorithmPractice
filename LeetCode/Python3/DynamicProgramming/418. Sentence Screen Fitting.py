# Given a rows x cols screen and a sentence represented by a list of non-empty words, 
# find how many times the given sentence can be fitted on the screen.

# Note:
# A word cannot be split into two lines.
# The order of words in the sentence must remain unchanged.
# Two consecutive words in a line must be separated by a single space.
# Total words in the sentence won't exceed 100.
# Length of each word is greater than 0 and won't exceed 10.
# 1 ≤ rows, cols ≤ 20,000.

# Example 1:
# Input:
# rows = 2, cols = 8, sentence = ["hello", "world"]
# Output: 
# 1
# Explanation:
# hello---
# world---
# The character '-' signifies an empty space on the screen.

# Example 2:
# Input:
# rows = 3, cols = 6, sentence = ["a", "bcd", "e"]
# Output: 
# 2
# Explanation:
# a-bcd- 
# e-a---
# bcd-e-
# The character '-' signifies an empty space on the screen.

# Example 3:
# Input:
# rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
# Output: 
# 1
# Explanation:
# I-had
# apple
# pie-I
# had--
# The character '-' signifies an empty space on the screen.

class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # 建表 查表
        # 若遇到起始为空格则新开一行排列，
        # 若单词被截断则回退到单词起始位置，另外起一行排列。

        # rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]
        # 'I had apple pie ' 16
        # 0 1 0 -1 -2 1 0 -1 -2 -3 -4 1 0 -1 -2 1
        
        s = ' '.join(sentence) + ' ' 
        counter = 0 
        move = [0] * len(s)
        
        for i in range(1, len(s)):
            move[i] = 1 if s[i] == ' ' else move[i-1]-1
            
        for _ in range(rows):
            counter += cols
            counter += move[counter % len(s)]
        return counter // len(s)