# Given a string S, find out the length of the longest repeating substring(s). 
# Return 0 if no repeating substring exists.

# Example 1:
# Input: "abcd"
# Output: 0
# Explanation: There is no repeating substring.

# Example 2:
# Input: "abbaba"
# Output: 2
# Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

# Example 3:
# Input: "aabcaabdaab"
# Output: 3
# Explanation: The longest repeating substring is "aab", which occurs 3 times.

# Example 4:
# Input: "aaaaa"
# Output: 4
# Explanation: The longest repeating substring is "aaaa", which occurs twice.
 
# Note:
# The string S consists of only lowercase English letters from 'a' - 'z'.
# 1 <= S.length <= 1500

# Hints:
# Generate all substrings in O(N^2) time with hashing.
# Choose those hashing of strings with the largest length.

# M1. linear search + set
class Solution1:
    def search(self, L: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            if tmp in seen:
                return start
            seen.add(tmp)
        return -1
        
    def longestRepeatingSubstring(self, S: str) -> str:
        # linear search
        n = len(S)
        for i in range(n-1, -1, -1):
            if self.search(i, n, S) != -1:
                return i 
            
# M2. binary search + set
class Solution2:
    def search(self, L: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            if tmp in seen:
                return start
            seen.add(tmp)
        return -1
        
    def longestRepeatingSubstring(self, S: str) -> str:

        n = len(S)
            
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, n, S) != -1:
                left = L + 1
            else:
                right = L - 1
        return left - 1

# M3. binary search + set(hash)
class Solution3:
    def search(self, L: int, n: int, S: str) -> str:
        """
        Search a substring of given length
        that occurs at least 2 times.
        @return start position if the substring exits and -1 otherwise.
        """
        seen = set()
        for start in range(0, n - L + 1):
            tmp = S[start:start + L]
            h = hash(tmp)
            if h in seen:
                return start
            seen.add(h)
        return -1
        
    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)
        
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, n, S) != -1:
                left = L + 1
            else:
                right = L - 1
               
        return left - 1

# M4. binary search + Rabin-Karp(Rolling hash) + avoid overflow
class Solution4:
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
        
    def longestRepeatingSubstring(self, S: str) -> str:
        n = len(S)
        # convert string to array of integers
        # to implement constant time slice
        nums = [ord(S[i]) - ord('a') for i in range(n)]
        # base value for the rolling hash function
        a = 26
        # modulus value for the rolling hash function to avoid overflow
        modulus = 2**24
        
        # binary search, L = repeating string length
        left, right = 1, n
        while left <= right:
            L = left + (right - left) // 2
            if self.search(L, a, modulus, n, nums) != -1:
                left = L + 1
            else:
                right = L - 1
               
        return left - 1