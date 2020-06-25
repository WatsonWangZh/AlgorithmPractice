# Given a string, sort it in decreasing order based on the frequency of characters.

# Example 1:

# Input:
# "tree"
# Output:
# "eert"
# Explanation:
# 'e' appears twice while 'r' and 't' both appear once.
# So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

# Example 2:
# Input:
# "cccaaa"
# Output:
# "cccaaa"
# Explanation:
# Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
# Note that "cacaca" is incorrect, as the same characters must be together.

# Example 3:
# Input:
# "Aabb"
# Output:
# "bbAa"
# Explanation:
# "bbaA" is also a valid answer, but "Aabb" is incorrect.
# Note that 'A' and 'a' are treated as two different characters.

import collections
import heapq
class Solution:
    def frequencySort(self, s: str) -> str:

        # M1. 模拟 O(nlogn) O(n)
        if not s: 
            return s
    
        # Convert s to a list.
        s = list(s)

        # Sort the characters in s.
        s.sort()

        # Make a list of strings, one for each unique char.
        all_strings = []
        cur_sb = [s[0]]
        for c in s[1:]:
            # If the last character on string builder is different...
            if cur_sb[-1] != c:
                all_strings.append("".join(cur_sb))
                cur_sb = []
            cur_sb.append(c)
        all_strings.append("".join(cur_sb))

        # Sort the strings by length from *longest* to shortest.
        all_strings.sort(key=lambda string : len(string), reverse=True)

        # Convert to a single string to return.
        # Converting a list of strings to a string is often done
        # using this rather strange looking python idiom.
        return "".join(all_strings)

        # ====================================
        # M2. 哈希表+排序 O(nlogn) O(n)
        # Count the occurence on each character
        cnt = collections.defaultdict(int)
        for c in s:
            cnt[c] += 1
	
        # Sort and Build string
        res = []
        for k, v in sorted(cnt.items(), key = lambda x: -x[1]):
            res += [k] * v
        return "".join(res)

        # ====================================
        # O(nlogk) O(n)
        # Count the occurence on each character
        cnt = collections.Counter(s)
        
        # Build string
        res = []
        for k, v in cnt.most_common():
            res += [k] * v
        return "".join(res)

        # ====================================
        # M3.哈希表 + 优先级队列 O(nlogk) O(n)
        # Count the occurence on each character
        cnt = collections.Counter(s)
        
        # Build heap
        heap = [(-v, k) for k, v in cnt.items()]
        heapq.heapify(heap)
        
        # Build string
        res = []
        while heap:
            v, k = heapq.heappop(heap)
            res += [k] * -v
        return ''.join(res)