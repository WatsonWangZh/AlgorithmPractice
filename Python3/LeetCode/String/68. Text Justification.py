# Given an array of words and a width maxWidth, 
# format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.
# You should pack your words in a greedy approach; that is, pack as many words as you can in each line. 
# Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line do not divide evenly between words, 
# the empty slots on the left will be assigned more spaces than the slots on the right.
# For the last line of text, it should be left justified and no extra space is inserted between words.

# Note:
# A word is defined as a character sequence consisting of non-space characters only.
# Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
# The input array words contains at least one word.

# Example 1:
# Input:
# words = ["This", "is", "an", "example", "of", "text", "justification."]
# maxWidth = 16
# Output:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]

# Example 2:
# Input:
# words = ["What","must","be","acknowledgment","shall","be"]
# maxWidth = 16
# Output:
# [
#   "What   must   be",
#   "acknowledgment  ",
#   "shall be        "
# ]
# Explanation: Note that the last line is "shall be    " instead of "shall     be",
#              because the last line must be left-justified instead of fully-justified.
#              Note that the second line is also left-justified becase it contains only one word.

# Example 3:
# Input:
# words = ["Science","is","what","we","understand","well","enough","to","explain",
#          "to","a","computer.","Art","is","everything","else","we","do"]
# maxWidth = 20
# Output:
# [
#   "Science  is  what we",
#   "understand      well",
#   "enough to explain to",
#   "a  computer.  Art is",
#   "everything  else  we",
#   "do                  "
# ]

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        # 模拟 逐行处理 拼接
        res = []
        self.words = words
        self.maxWidth = maxWidth
        while len(self.words) != 0:
            res.append(self.fillOneLine())
        return res

    def fillOneLine(self):
        line = ''
        length = len(self.words[0])
        lastIdx = 0

        # 找出每行最多可以放的单词数量，逐行处理
        for i,word in enumerate(self.words[1:]):
            length += len(word) + 1
            lastIdx = i+1
            if length > self.maxWidth:
                lastIdx = i
                length -= (len(word)+1)
                break


        leftSpace = self.maxWidth - length
        # 特殊处理最后一行空格的填补
        if lastIdx == len(self.words)-1:
            line = ' '.join(self.words) + ' ' * leftSpace
        else:
            # 处理首行单个单词问题 （除0异常）
            if lastIdx == 0:
                line = self.words[0] + ' ' * leftSpace
            else:
                q, r = divmod((lastIdx + leftSpace), lastIdx)
                # 空格可以平均分配
                if r==0:
                    line = (' '*q).join(self.words[:lastIdx+1])
                # 不能平均分配时，左边空格数量要多于右边
                else:
                    line = (' '*(q+1)).join(self.words[:r+1]) + ' '*q + (' '*q).join(self.words[r+1:lastIdx+1])

        self.words = self.words[lastIdx+1:]
        return line
