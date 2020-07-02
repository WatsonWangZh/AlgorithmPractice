# Given a string s, return all the palindromic permutations (without duplicates) of it. 
# Return an empty list if no palindromic permutation could be form.

# Example 1:
# Input: "aabb"
# Output: ["abba", "baab"]

# Example 2:
# Input: "abc"
# Output: []

# Hints:
# If a palindromic permutation exists, we just need to generate the first half of the string.
# To generate all distinct permutations of a (half of) string, use a similar approach from: Permutations II or Next Permutation.

class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # 这道题是之前那道Palindrome Permutation的拓展，那道题只是让判断存不存在回文全排列，而这题让我们返回所有的回文全排列，
        # 此题给了我们充分的提示：如果回文全排列存在，我们只需要生成前半段字符串即可，后面的直接根据前半段得到。
        # 那么我们再进一步思考，由于回文字符串有奇偶两种情况，偶数回文串例如abba，可以平均分成前后半段，
        # 而奇数回文串例如abcba，需要分成前中后三段，需要注意的是中间部分只能是一个字符，
        # 那么我们可以分析得出，如果一个字符串的回文字符串要存在，那么奇数个的字符只能有0个或1个，其余的必须是偶数个，
        # 所以我们可以用哈希表来记录所有字符的出现个数，然后我们找出出现奇数次数的字符加入mid中，
        # 如果有两个或两个以上的奇数个数的字符，那么返回空集，
        # 我们对于每个字符，不管其奇偶，都将其个数除以2的个数的字符加入t中，
        # 这样做的原因是如果是偶数个，那么将其一般加入t中，如果是奇数，如果有1个，那么除以2是0，不会有字符加入t，
        # 如果是3个，那么除以2是1，取一个加入t。
        # 等我们获得了t之后，t是就是前半段字符，
        # 我们对其做全排列，每得到一个全排列，我们加上mid和该全排列的逆序列就是一种所求的回文字符串，
        # 这样我们就可以得到所有的回文全排列了。
        # 在全排序的子函数中有一点需要注意的是，如果我们直接用数组来保存结果时，并且t中如果有重复字符的话可能会出现重复项。
        
        m = {}
        res = []
        even = []
        odd = ''
        half = []
        
        if self.canBePalindromes(s, m) == False:
            return res
        
        for i in m.keys():
            if m[i] % 2 == 0:
                for t in range(m[i]//2):
                    even.append(i)
            else:
                odd += i
                if m[i] > 1:
                    for t in range(m[i]//2):
                        even.append(i)

        even.sort()
        
        self.permutationHalf('', [], even, half)
        
        self.completeOtherHalf(half, odd, res)
        
        return res
        
        
        
    def completeOtherHalf(self, half, odd, res):
        for item in half:
            temp = item + odd
            for i in range(len(item)-1, -1, -1):
                temp += item[i]
                
            res.append(temp)
            
            
    
    def permutationHalf(self, curr, currIdx, even, half): 
        if len(curr) == len(even):
            half.append(curr)
            return
        pre = ''
        for i in range(len(even)):
            if i not in currIdx and even[i] != pre:
                pre = even[i]
                self.permutationHalf(curr + even[i], currIdx + [i], even, half)
            
    
    
    def canBePalindromes(self, s, m):
        l = len(s)
        
        count = 0
        for i in range(l):
            if s[i] in m:
                m[s[i]] += 1
            else:
                m[s[i]] = 1
                
        for n in m.keys():
            if m[n] % 2 == 1:
                count += 1
            if count > 1:
                return False
                break
                
        return True