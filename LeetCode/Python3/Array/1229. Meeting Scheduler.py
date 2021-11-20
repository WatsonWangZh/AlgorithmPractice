# Given the availability time slots arrays slots1 and slots2 of two people and a meeting duration duration, 
# return the earliest time slot that works for both of them and is of duration duration.
# If there is no common time slot that satisfies the requirements, return an empty array.
# The format of a time slot is an array of two elements [start, end] representing an inclusive time range from start to end.  
# It is guaranteed that no two availability slots of the same person intersect with each other. 
# That is, for any two time slots [start1, end1] and [start2, end2] of the same person, either start1 > end2 or start2 > end1.

# Example 1:
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 8
# Output: [60,68]

# Example 2:
# Input: slots1 = [[10,50],[60,120],[140,210]], slots2 = [[0,15],[60,70]], duration = 12
# Output: []
 
# Constraints:
# 1 <= slots1.length, slots2.length <= 10^4
# slots1[i].length, slots2[i].length == 2
# slots1[i][0] < slots1[i][1]
# slots2[i][0] < slots2[i][1]
# 0 <= slots1[i][j], slots2[i][j] <= 10^9
# 1 <= duration <= 10^6 

# Hints:
# Assume that in the solution, the selected slot from slotsA is bigger than the respectively selected slot from slotsB.
# Use two pointers in order to try all the possible intersections, and check the length.
# Do the same in step N° 1 but now assume that the selected slot from slotsB is bigger, return the minimum of the two options.

class Solution(object):
    def minAvailableDuration(self, slots1, slots2, duration):
        """
        :type slots1: List[List[int]]
        :type slots2: List[List[int]]
        :type duration: int
        :rtype: List[int]
        """
        # 贪心 双指针 O(n+m)

        slots1.sort(key=lambda x: x[0])
        slots2.sort(key=lambda x: x[0])
        i, j = 0, 0
        n, m = len(slots1), len(slots2)
        res = []
        
        while i < n and j < m:
            while i < n and slots1[i][1] < slots2[j][0]:
            # while slots1[i][1] < slots2[j][0] and i < n: gets list index out of range wrong. why? 
                i += 1
                
            if i == n:
                break
            
            while j < m and slots2[j][1] < slots1[i][0]:
            # while slots2[j][1] < slots1[i][0] and j < m:  gets list index out of range wrong. why?                
                j += 1
                
            if j == m:
                break

            s1, e1, s2, e2 = slots1[i][0], slots1[i][1], slots2[j][0], slots2[j][1]
            if s2 <= s1 <= e2:
                dura = min(e1, e2) - s1
                if dura >= duration:
                    res.append(s1)
                    res.append(s1+duration)
                    break # key
                else:
                    if e1 < e2:
                        i += 1
                    else:
                        j += 1
                    
            elif s1 <= s2 <= e1:
                dura = min(e1, e2) - s2
                if dura >= duration:
                    res.append(s2)
                    res.append(s2+duration)
                    break #key
                else:
                    if e1 < e2:
                        i += 1
                    else:
                        j += 1

        return res

