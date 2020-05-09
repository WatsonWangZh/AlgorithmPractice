# Sometimes people repeat letters to represent extra feeling, 
# such as "hello" -> "heeellooo", "hi" -> "hiiii".  
# In these strings like "heeellooo", 
# we have groups of adjacent letters that are all the same:  "h", "eee", "ll", "ooo".
# For some given string S, a query word is stretchy 
# if it can be made to be equal to S by any number of applications of the following extension operation: 
# choose a group consisting of characters c, 
# and add some number of characters c to the group so that the size of the group is 3 or more.
# For example, starting with "hello", 
# we could do an extension on the group "o" to get "hellooo", 
# but we cannot get "helloo" since the group "oo" has size less than 3.  
# Also, we could do another extension like "ll" -> "lllll" to get "helllllooo".  
# If S = "helllllooo", then the query word "hello" would be stretchy 
# because of these two extension operations: query = "hello" -> "hellooo" -> "helllllooo" = S.
# Given a list of query words, return the number of words that are stretchy. 

# Example:
# Input: 
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1
# Explanation: 
# We can extend "e" and "o" in the word "hello" to get "heeellooo".
# We can't extend "helo" to get "heeellooo" because the group "ll" is not size 3 or more.
 
# Notes:
# 0 <= len(S) <= 100.
# 0 <= len(words) <= 100.
# 0 <= len(words[i]) <= 100.
# S and all words in words consist only of lowercase letters
 

class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        res = 0
        set_S = set(S)
        S_list = []
        pre_s, pre_index = S[0], 0
        for i, s in enumerate(S):
            if pre_s != s:
                S_list.append(S[pre_index:i])
                pre_s, pre_index = s, i
            if i == len(S) - 1:
                S_list.append(S[pre_index:])
                
        for word in words:
            if set(word) != set_S:
                continue
                
            word_list = []
            pre_w, pre_index = word[0], 0
            for i, w in enumerate(word):
                if pre_w != w:
                    word_list.append(word[pre_index:i])
                    pre_w, pre_index = w, i
                if i == len(word) - 1:
                    word_list.append(word[pre_index:])
                    
            if len(S_list) == len(word_list):
                if all(S_list[i] == word_list[i] if len(S_list[i]) < 3\
                     else len(S_list[i]) >= len(word_list[i])\
                          for i in range(len(S_list))):
                    res += 1
        return res
