# Given a non-empty string s and an abbreviation abbr, 
# return whether the string matches with the given abbreviation.
# A string such as "word" contains only the following valid abbreviations:
# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", 
# "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Notice that only the above abbreviations are valid abbreviations of the string "word". 
# Any other string is not a valid abbreviation of "word".

# Note:
# Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

# Example 1:
# Given s = "internationalization", abbr = "i12iz4n":
# Return true.

# Example 2:
# Given s = "apple", abbr = "a2e":
# Return false.

class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        i = j = 0
        
        while i < len(word) and j < len(abbr):
            
            if word[i] == abbr[j]:
                i += 1
                j += 1
                
            elif abbr[j] <= '0' or abbr[j] > '9':
                return False
            
            elif abbr[j].isdigit():
                k = j
                while k < len(abbr):
                    if abbr[k].isdigit():
                        k += 1
                    else:
                        break
                i += int(abbr[j:k])
                j = k
                
            else:
                return False
            
        return True if len(word) == i and len(abbr) == j else False
        