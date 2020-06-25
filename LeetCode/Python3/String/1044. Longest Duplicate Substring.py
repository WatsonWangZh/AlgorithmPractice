# Given a string S, 
# consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  
# (The occurrences may overlap.)
# Return any duplicated substring that has the longest possible length.  
# (If S does not have a duplicated substring, the answer is "".)

# Example 1:
# Input: "banana"
# Output: "ana"

# Example 2:
# Input: "abcd"
# Output: ""
 
# Note:
# 2 <= S.length <= 10^5
# S consists of lowercase English letters.

# Hints:
# Binary search for the length of the answer. 
# (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
# To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.

# bianry search + Rabin-Karp(Rolling hash) + avoid overflow
class Solution:
    def search(self, L: int, a: int, modulus: int, n: int, nums: List[int]) -> str:
        """
        Rabin-Karp with polynomial rolling hash.
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        # compute the hash of string S[:L]
        h = 0
        for i in range(L):
            h = (h * a + nums[i]) % modulus
              
        # already seen hashes of strings of length L
        seen = {h} 
        # const value to be used often : a**L % modulus
        aL = pow(a, L, modulus) 
        for start in range(1, n - L + 1):
            # compute rolling hash in O(1) time
            h = (h * a - nums[start - 1] * aL + nums[start + L - 1]) % modulus
            if h in seen:
                return start
            seen.add(h)
        return -1
        
    def longestDupSubstring(self, S: str) -> str:
        n = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**32
        
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L - 1
               
        start = self.search(left - 1, a, modulus, n, nums)
        return S[start: start + left - 1]
             