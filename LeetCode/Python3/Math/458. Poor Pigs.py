# There are 1000 buckets, one and only one of them is poisonous, while the rest are filled with water. 
# They all look identical. If a pig drinks the poison it will die within 15 minutes. 
# What is the minimum amount of pigs you need to figure out which bucket is poisonous within one hour?
# Answer this question, and write an algorithm for the general case.
# General case:
# If there are n buckets and a pig drinking poison will die within m minutes, 
# how many pigs (x) you need to figure out the poisonous bucket within p minutes? 
# There is exactly one bucket with poison.

# Note:
# A pig can be allowed to drink simultaneously on as many buckets as one would like, and the feeding takes no time.
# After a pig has instantly finished drinking buckets, there has to be a cool down time of m minutes. 
# During this time, only observation is allowed and no feedings at all.
# Any given bucket can be sampled an infinite number of times (by an unlimited number of pigs).

# Hints:
# What if you only have one shot? Eg. 4 buckets, 15 mins to die, and 15 mins to test.
# How many states can we generate with x pigs and T tests?
# Find minimum x such that (T+1)^x >= N

class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        # 数学 O(logn)
        # 1） 一只猪在一小时内最多能验多少桶？
        # 0min喝1号桶，15min后没挂再喝2号桶，60min内可以喝 60/15 = 4 次。如果有5桶水，那个只要喝前4桶就只能第5桶是否有毒。
        # 因此一只猪在一小时可以验5桶水。
        # 2）两只猪在一小时内最多能验多少桶？
        # 既然一只猪能验5桶，那么用二维思路，2只猪应该可以验5*5桶：
        # 猪A负责行，猪B负责列，每15分钟试喝一行/一列的所有5桶水，通过2只猪上天的时间能推断出毒水在几行几列。
        # 1 2 3 4 5
        # 6 7 8 9 10
        # 11 12 13 14 15
        # 16 17 18 19 20
        # 21 22 23 24 25
        # 3）推到N只猪，则5^N >= 1000，最小的N即为所求。

        # 调包
        # import math
        # times = minutesToTest // minutesToDie + 1
        # return int(math.ceil(math.log(buckets, times)))

        # 不调包
        times = minutesToTest // minutesToDie + 1
        pigs = 0
        while times ** pigs < buckets:
            pigs += 1
        return pigs
