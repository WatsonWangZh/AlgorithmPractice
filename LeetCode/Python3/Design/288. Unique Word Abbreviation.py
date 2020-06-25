# An abbreviation of a word follows the form <first letter><number><last letter>. 
# Below are some examples of word abbreviations:
# a) it                      --> it    (no abbreviation)
#      1
#      ↓
# b) d|o|g                   --> d1g
#               1    1  1
#      1---5----0----5--8
#      ↓   ↓    ↓    ↓  ↓    
# c) i|nternationalizatio|n  --> i18n
#               1
#      1---5----0
#      ↓   ↓    ↓
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. 
# A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

# Example:
# Given dictionary = [ "deer", "door", "cake", "card" ]
# isUnique("dear") -> false
# isUnique("cart") -> true
# isUnique("cane") -> false
# isUnique("make") -> true

# M1
# class ValidWordAbbr(object):

#     def __init__(self, dictionary):
#         """
#         :type dictionary: List[str]
#         """
#         self.dic = {}

#         if not dictionary or not dictionary[0]:
#             return
        
#         for i in range(len(set(dictionary))):
#             temp = dictionary[i][0] + str(len(dictionary[i])-2) + dictionary[i][-1]
#             if temp not in self.dic:
#                 self.dic[temp] = dictionary[i]
#             else:
#                 self.dic[temp] = ""

#         # print(self.dic)

#     def isUnique(self, word):
#         """
#         :type word: str
#         :rtype: bool
#         """
#         if not word:
#             return True
#         pro_word = word[0] + str(len(word)-2) + word[-1]
        
#         return pro_word in self.dic.keys() and self.dic[pro_word] == word or pro_word not in self.dic.keys()

# M2
class ValidWordAbbr(object):

    def __init__(self, dictionary):
        """
        :type dictionary: List[str]
        """
        self.exist = {}
        for word in set(dictionary):
            if word:
                abbrev = (word[0], word[-1], len(word))
                # consider if the dict only contains one word "hello", and then call isUnique with "hello"
                # it is still unique because it is the same to the item in the dict
                if abbrev not in self.exist:
                    self.exist[abbrev] = word
                elif self.exist[abbrev]:
                    self.exist[abbrev] = ""

    def isUnique(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if not word:
            return True
        abbrev = (word[0], word[-1], len(word))
        return abbrev not in self.exist or self.exist[abbrev] == word

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)