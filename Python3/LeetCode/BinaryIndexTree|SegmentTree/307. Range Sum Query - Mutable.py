# Given an integer array nums, 
# find the sum of the elements between indices i and j (i ≤ j), inclusive.
# The update(i, val) function modifies nums by updating the element at index i to val.

# Example:
# Given nums = [1, 3, 5]
# sumRange(0, 2) -> 9
# update(1, 2)
# sumRange(0, 2) -> 8

# Note:
# The array is only modifiable by the update function.
# You may assume the number of calls to update and sumRange function is distributed evenly.

class NumArray:

    # M1.Naive Method
    # Time Limit Exceeded
    # def __init__(self, nums: List[int]):
    #     self.nums = nums

    # def update(self, i: int, val: int) -> None:
    #     self.nums[i] = val
    
    # def sumRange(self, i: int, j: int) -> int:
    #     sum = 0
    #     for _ in range(i,j+1):
    #         sum += self.nums[_]
    #     return sum

    # M2. Sqrt Decomposition O(n)
    # def __init__(self, nums):
    #     self.width = int(len(nums)**0.5)    # width of each bin (apart from last)
    #     self.bin_sums = []                  # sum of each bin
    #     self.nums = nums
    #     for i, num in enumerate(nums):
    #         if i % self.width == 0:         # start a new bin
    #             self.bin_sums.append(num)
    #         else:                           # add to last bin
    #             self.bin_sums[-1] += num

    # def update(self, i, val):
    #     bin_i = i // self.width
    #     diff = val - self.nums[i]
    #     self.bin_sums[bin_i] += diff        # update bin_sums
    #     self.nums[i] = val                  # update nums

    # def sumRange(self, i, j):
    #     bin_i, bin_j = i // self.width, j // self.width
    #     range_sum = sum(self.bin_sums[bin_i:bin_j])         # sum of whole bins 
    #     range_sum += sum(self.nums[bin_j*self.width:j+1])   # add partial last bin
    #     range_sum -= sum(self.nums[bin_i*self.width:i])     # subtract partial first bin
    #     return range_sum

    # M3.FenwickTree(树状树组) O(lgn)
    # https://www.youtube.com/watch?v=WbafSgetDDk
    def __init__(self, nums: List[int]):
        self.array = [0] + nums
        self.nums = nums
        for i in range(1, len(self.array)):
            i2 = i + (i & -i)  #lowbit(i)
            if i2 < len(self.array):
                self.array[i2] += self.array[i]

    def update(self, i: int, val: int) -> None:
        i += 1
        diff, self.nums[i-1] = val - self.nums[i-1], val
        while i < len(self.array):
            self.array[i] += diff
            i += (i & -i) #lowbit(i)
    
    def prefix_sum(self, idx):
        idx += 1
        result = 0
        while idx:
            result += self.array[idx]
            idx -= idx & -idx

    def sumRange(self, i: int, j: int) -> int:
        return self.prefix_sum(j) - self.prefix_sum(i-1)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)