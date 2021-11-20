# Given a list of strings, you could concatenate these strings together into a loop, 
# where for each string you could choose to reverse it or not. 
# Among all the possible loops, you need to find the lexicographically biggest string after cutting the loop, 
# which will make the looped string into a regular one.
# Specifically, to find the lexicographically biggest string, you need to experience two phases:
# Concatenate all the strings into a loop, 
# where you can reverse some strings or not and connect them in the same order as given.
# Cut and make one breakpoint in any place of the loop, 
# which will make the looped string into a regular one starting from the character at the cutpoint.
# And your job is to find the lexicographically biggest one among all the possible regular strings.

# Example:
# Input: "abc", "xyz"
# Output: "zyxcba"
# Explanation: You can get the looped string "-abcxyz-", "-abczyx-", "-cbaxyz-", "-cbazyx-", where '-' represents the looped status. 
# The answer string came from the fourth looped one, where you could cut from the middle character 'a' and get "zyxcba".

# Note:
# The input strings will only contain lowercase letters.
# The total length of all the strings will not over 1,000.

class Solution(object):
    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # https://www.cnblogs.com/grandyang/p/6887140.html
        # M1. 枚举切分位置 O(n^2)
        strs, res = [x if x >= x[::-1] else x[::-1] for x in strs],''
        for i, can in enumerate(strs):
            rest = ''.join(strs[i+1:] + strs[:i])
            for can in (can, can[::-1]):
                for j in range(len(can)):
                    tmp = can[j:] + rest + can[:j]
                    res = max(res, tmp)
        return res
        
        # M2. 最高位优先减少枚举数量 O(n^2)
        lst = []
        maxChar = 'a'
        for i in range(len(strs)):
            strs[i] = strs[i][::-1] if strs[i] < strs[i][::-1] else strs[i]
            for pos, c in enumerate(strs[i]):
                if c > maxChar:
                    maxChar = c
                    lst = [(i, pos)]
                elif c == maxChar:
                    lst.append((i, pos))
        res = ''
        for i, pos in lst:
            string = strs[i]
            mid = "".join(strs[i+1:]) + "".join(strs[:i]) 
            for head, tail in ((string[pos:], string[:pos]), (string[:pos+1][::-1], string[pos+1:][::-1])):
                tmp = head + mid + tail
                res = max(res, tmp)
        return res