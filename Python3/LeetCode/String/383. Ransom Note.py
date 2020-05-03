# Given an arbitrary ransom note string and another string containing letters from all the magazines, 
# write a function that will return true if the ransom note can be constructed from the magazines ; 
# otherwise, it will return false.
# Each letter in the magazine string can only be used once in your ransom note.

# Note:
# You may assume that both strings contain only lowercase letters.

# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

import collections
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # M1. 模拟
        # For each character, c,  in the ransom note.
        for c in ransomNote:
        # If there are none of c left in the String, return False.
            if c not in magazine:
                return False
            # Find the index of the first occurrence of c in the magazine.
            location = magazine.index(c)
            # Use splicing to make a new string with the characters 
            # before "location" (but not including), and the characters 
            #after "location". 
            magazine = magazine[:location] + magazine[location + 1:]
        # If we got this far, we can successfully build the note.
        return True

        # M2. 哈希表
        # 双哈希表
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        magazine_counts = collections.Counter(magazine)
        ransom_note_counts = collections.Counter(ransomNote)
    
        # For each *unique* character in the ransom note:
        for char, count in ransom_note_counts.items():
            # Check that the count of char in the magazine is equal
            # or higher than the count in the ransom note.
            magazine_count = magazine_counts[char]
            if magazine_count < count:
                return False
            
        # If we got this far, we can successfully build the note.
        return True 

        # 单哈希表
        # Check for obvious fail case.
        if len(ransomNote) > len(magazine): return False

        # In Python, we can use the Counter class. It does all the work that the
        # makeCountsMap(...) function in our pseudocode did!
        letters = collections.Counter(magazine)
    
        # For each character, c, in the ransom note:
        for c in ransomNote:
            # If there are none of c left, return False.
            if letters[c] <= 0:
                return False
            # Remove one of c from the Counter.
            letters[c] -= 1
        # If we got this far, we can successfully build the note.
        return True
