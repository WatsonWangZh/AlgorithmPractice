# The set [1,2,3,...,n] contains a total of n! unique permutations.
# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.
# Note:
# Given n will be between 1 and 9 inclusive.
# Given k will be between 1 and n! inclusive.

# Example 1:
# Input: n = 3, k = 3
# Output: "213"

# Example 2:
# Input: n = 4, k = 9
# Output: "2314"

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 规律计数  实现技巧 O(n^2)
        # 做法：
        # 从高位到低位依次考虑每一位；
        # 对于每一位，从小到大依次枚举未使用过的数，确定当前位是几；
        # 为了便于理解，我们这里给出一个例子的具体操作：n=4,k=14。
        # 首先我们将所有排列按首位分组：
        # 1 + (2, 3, 4的全排列)
        # 2 + (1, 3, 4的全排列)
        # 3 + (1, 2, 4的全排列)
        # 4 + (2, 3, 4的全排列)
        # 接下来我们确定第 k=14 个排列在哪一组中。每组的排列个数是 3!=6 个，所以第14个排列在第3组中，所以首位已经可以确定，是3。
        # 然后我们再将第3组的排列继续分组：
        # 31 + (2, 4的全排列)
        # 32 + (1, 4的全排列)
        # 34 + (1, 2的全排列)
        # 接下来我们判断第 k=14 个排列在哪个小组中。我们先求第 14 个排列在第三组中排第几，由于前两组每组有6个排列，所以第14个排列在第3组排第 14−6∗2=2。
        # 在第三组中每个小组的排列个数是 2!=2个，所以第 k 个排列在第1个小组，所以可以确定它的第二位数字是1。
        # 依次类推，可以推出第14个排列是 3142。
        # 时间复杂度分析：两重循环，所以时间复杂度是 O(n^2)。

        import math
        res = ""
        vals = [str(i) for i in range(1, n+1)]
        while vals:
            f = math.factorial(n-1)
            idx = (k-1) // f
            r = (k-1) % f + 1
            res += vals[idx]
            del vals[idx]
            k = r
            n -= 1
        return res

# Solution based on Leetcode 46. Permutations, Got TLE. 
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        
        return ''.join(self.permute([str(i) for i in range(1, n+1)])[k-1])
    
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        temp = []
        visited = [False] * len(nums)
        self.dfs(nums, 0, temp, res, visited)
        return res

    def dfs(self, nums, pos, temp, res, visited):
        if pos == len(nums):
            res.append(temp[:])
            return 

        for i in range(len(nums)):
            if not visited[i]:
                visited[i] = True
                temp.append(nums[i])
                self.dfs(nums, pos+1, temp, res, visited)
                visited[i] = False
                temp.pop()

# Solution based on Leetcode 31. next Permutation
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        import math
        k = k % (math.factorial(n)+1)
        nums = [i+1 for i in range(n)]  # 1st permutation of nums
        for i in range(k-1):
            nums = self.nextPermutation(nums)
        return "".join([ str(ch) for ch in nums])

    def nextPermutation(self, nums):

        n = len(nums)
        i,j = n-1, n-1

        # From right to left, find the first decreasing number
        while i > 0 and nums[i] <= nums[i-1]:
            i -= 1 
        
        # [3,2,1] -> [1,2,3]
        if i==0: 
            nums[:]=nums[::-1]
            return nums

        # From right to left, finding number just larget than the first decreasing number
        for j in range(n-1, i-1, -1):
            if nums[j] > nums[i-1]:
                break 
             
        # Swap 
        nums[j], nums[i-1] = nums[i-1], nums[j]

        # Reversing the backend numbers
        nums[i:] = nums[i:][::-1]

        return nums
    
