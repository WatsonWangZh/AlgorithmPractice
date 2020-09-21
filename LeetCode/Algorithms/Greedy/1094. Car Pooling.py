# You are driving a vehicle that has capacity empty seats initially available for passengers.  
# The vehicle only drives east (ie. it cannot turn around and drive west.)
# Given a list of trips, trip[i] = [num_passengers, start_location, end_location] 
# contains information about the i-th trip: the number of passengers that must be picked up, 
# and the locations to pick them up and drop them off.  
# The locations are given as the number of kilometers due east from your vehicle's initial location.
# Return true if and only if it is possible to pick up and drop off all passengers for all the given trips. 

# Example 1:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 4
# Output: false

# Example 2:
# Input: trips = [[2,1,5],[3,3,7]], capacity = 5
# Output: true

# Example 3:
# Input: trips = [[2,1,5],[3,5,7]], capacity = 3
# Output: true

# Example 4:
# Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
# Output: true
 
# Constraints:
# trips.length <= 1000
# trips[i].length == 3
# 1 <= trips[i][0] <= 100
# 0 <= trips[i][1] < trips[i][2] <= 1000
# 1 <= capacity <= 100000

# Hints:
# Sort the pickup and dropoff events by location, then process them in order.

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # 预处理 + 模拟
        stops = [0] * 1001
        
        for trip in trips:
            #上车
            stops[trip[1]] += trip[0]
            #下车
            stops[trip[2]] -= trip[0]
            
        cur = 0
        for p in stops:
            cur += p
            if cur > capacity:
                return False
            
        return True