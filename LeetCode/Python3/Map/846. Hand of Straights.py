# Alice has a hand of cards, given as an array of integers.
# Now she wants to rearrange the cards into groups 
# so that each group is size W, and consists of W consecutive cards.
# Return true if and only if she can.

# Example 1:
# Input: hand = [1,2,3,6,2,3,4,7,8], W = 3
# Output: true
# Explanation: Alice's hand can be rearranged as [1,2,3],[2,3,4],[6,7,8].

# Example 2:
# Input: hand = [1,2,3,4,5], W = 4
# Output: false
# Explanation: Alice's hand can't be rearranged into groups of 4.

# Note:
# 1 <= hand.length <= 10000
# 0 <= hand[i] <= 10^9
# 1 <= W <= hand.length

import collections
class Solution:
    # 这道题说是我们在打扑克牌，是否能将手里的牌都以顺子的形式出完。
    # 由于牌可以重复，所以我们要统计每张牌出现的次数，同时还要给牌按大小排序，
    # 那么用Counter来建立牌的大小和其出现次数之间的映射就最好不过了，
    # 利用了其可以按key值排序的特点。首先遍历手中牌，建立映射。
    # 然后开始循环，条件是Counter不为空，然后取出最小的那张牌，然后遍历能组成顺子的W张牌，
    # 若没有直接返回False，有的话，则映射值自减1，若映射值为0了，则从Counter中移除该映射对即可，
    # 循环退出后返回True。

    def isNStraightHand(self, hand, W):
        if not hand or len(hand) % W:
            return False
        
        counter = collections.Counter(hand)
        while counter:
            elem = min(counter)
            cnt = 0
            while cnt < W:
                if elem not in counter:
                    return False
                counter[elem] -= 1
                if not counter[elem]:
                    del counter[elem]
                elem += 1
                cnt += 1
                
        return True
        

