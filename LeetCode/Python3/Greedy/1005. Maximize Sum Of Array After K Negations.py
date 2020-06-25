# Given an array A of integers, we must modify the array in the following way: 
# we choose an i and replace A[i] with -A[i], and we repeat this process K times in total.  
# (We may choose the same index i multiple times.)
# Return the largest possible sum of the array after modifying it in this way.

# Example 1:
# Input: A = [4,2,3], K = 1
# Output: 5
# Explanation: Choose indices (1,) and A becomes [4,-2,3].

# Example 2:
# Input: A = [3,-1,0,2], K = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and A becomes [3,1,0,2].

# Example 3:
# Input: A = [2,-3,-1,5,-4], K = 2
# Output: 13
# Explanation: Choose indices (1, 4) and A becomes [2,3,-1,5,4].

# Note:
# 1 <= A.length <= 10000
# 1 <= K <= 10000
# -100 <= A[i] <= 100

from collections import heapq
class Solution:
    # 这个题稍微一分析就知道：我们优先翻转负数翻转成正数，这样和就会变大。
    # 那么优先翻转哪个负数呢？肯定是最小的负数，这样求相反数之后会变得最大。
    # 那么，当负数翻转完了之后怎么办？那么只能翻转非负数了，所以如果有0就一直翻转0，
    # 否则就每次挑正数翻转成负数，翻转之后继续选负数翻转。
    # 总而言之：维护一个最小堆，每次翻转堆里面的最小数字，翻转之后的结果仍然放入堆中以便下次翻转。
    # 每次翻转之后和会增加二倍翻转的数字的相反数。所以，不要每次翻转之后都去求和，而应该在刚开始的时候求一次和就行

    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        _sum = sum(A)
        heapq.heapify(A)
        while K > 0:
            curmin = heapq.heappop(A)
            heapq.heappush(A, -curmin)
            K -= 1
            _sum += -curmin * 2;
        return _sum
