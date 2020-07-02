# Given an encoded string, return its decoded string.
# The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. 
# Note that k is guaranteed to be a positive integer.
# You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. 
# For example, there won't be input like 3a or 2[4].

# Examples:
# s = "3[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        # M1. 递归
        res = ''
        i = 0
        while i < len(s):
            if not s[i].isdigit() and s[i] != '[' and s[i] != ']':
                res += s[i]
                i += 1
            else:
                # Get repeat-times
                j = i
                while '0' <= s[j] <= '9':
                    j += 1
                repeat = int(s[i:j])

                # Get the strings between square brackets
                cnt = 0
                i = j + 1
                while i < len(s) and cnt >= 0:
                    if s[i] == '[':
                        cnt += 1
                    elif s[i] == ']':
                        cnt -= 1
                    i += 1

                res += repeat * self.decodeString(s[j+1:i-1])
        return res

        # M2. 栈
    
        num = 0
        stack = [['', '']]
        for c in s:
            if '0' <= c <= '9':
                num = num * 10 + ord(c) - 48
            elif c == '[':
                stack.append([num, ''])
                num = 0
            elif c == ']':
                repeat, substr = stack.pop()
                stack[-1][1] += repeat * substr
            else:
                stack[-1][1] += c
        return stack[0][1]
