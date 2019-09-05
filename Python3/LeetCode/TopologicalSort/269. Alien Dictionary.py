# There is a new alien language which uses the latin alphabet. 
# However, the order among letters are unknown to you. 
# You receive a list of non-empty words from the dictionary, 
# where words are sorted lexicographically by the rules of this new language. 
# Derive the order of letters in this language.

# Example 1:
# Input:
# [
#   "wrt",
#   "wrf",
#   "er",
#   "ett",
#   "rftt"
# ]
# Output: "wertf"

# Example 2:
# Input:
# [
#   "z",
#   "x"
# ]
# Output: "zx"

# Example 3:
# Input:
# [
#   "z",
#   "x",
#   "z"
# ] 
# Output: "" 
# Explanation: The order is invalid, so return "".

# Note:
# You may assume all letters are in lowercase.
# You may assume that if a is a prefix of b, then a must appear before b in the given dictionary.
# If the order is invalid, return an empty string.
# There may be multiple valid order of letters, return any one of them is fine.

import collections
class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # https://www.youtube.com/watch?v=RIrTuf4DfPE
        # 图的构建，拓扑遍历 

        degree = collections.defaultdict(int)   # character and the in-degree
        charGraph = collections.defaultdict(set)    # a graph between the characters

        # Step1 : Degree Map of each character.

        for i in range(0, len(words)):
            for char in words[i]:
                degree[char] = 0

        # Step2: Build graph using the sorted words array.
        # If two chars are at the same position and different then char that appearsin word1 comes before char in word 2.

        for i in range(0, len(words)-1): # Words are sorted lexicographically.
            word1 = words[i]
            word2 = words[i+1]
            sm_word_len = min(len(word1), len(word2))

            for j in range(0, sm_word_len):
                c1 = word1[j]
                c2 = word2[j]
                if c1 != c2:
                    if c2 not in charGraph[c1]:
                        charGraph[c1].add(c2) # word
                        degree[c2] += 1
                    break

        # Step 3: Perform Topological sort using Kahn's algorithm using Degree Map and Graph in Step 1 and 2.
        queue = collections.deque([])
        result = ""
        for k, v in degree.items():
            if not v: 
                queue.append(k)

        # Kahn's algo.
        # https://en.wikipedia.org/wiki/Topological_sorting
        while queue:
            node = queue.popleft()
            result += node
            for n in charGraph[node]:
                degree[n] -= 1
                # incase a disconnected graph.
                if degree[n] == 0: 
                    queue.append(n)
        
        # Step 4: Check the result is Reasonable.
        if len(result) == len(degree):
            return result
        else:
            return ""
