# We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
# (Here, the distance between two points on a plane is the Euclidean distance.)
# You may return the answer in any order.  
# The answer is guaranteed to be unique (except for the order that it is in.)

# Example 1:
# Input: points = [[1,3],[-2,2]], K = 1
# Output: [[-2,2]]
# Explanation: 
# The distance between (1, 3) and the origin is sqrt(10).
# The distance between (-2, 2) and the origin is sqrt(8).
# Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
# We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

# Example 2:
# Input: points = [[3,3],[5,-1],[-2,4]], K = 2
# Output: [[3,3],[-2,4]]
# (The answer [[-2,4],[3,3]] would also be accepted.)
 
# Note:
# 1 <= K <= points.length <= 10000
# -10000 < points[i][0] < 10000
# -10000 < points[i][1] < 10000

class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        # M1. 库函数找TopK O(nlgn)
        points.sort(key=lambda x: pow(x[0], 2) + pow(x[1], 2))
        return points[:K]

        # M2. 分治找出top K O(n)
        # 计算欧几里得距离
        distance = lambda i: points[i][0] ** 2 + points[i][1] ** 2
        
        def helper(i, j, K):
            if i > j:
                return
            # 记录初始值
            oi, oj = i, j
            # 取最左边为哨兵值
            pivot = distance(oi)
            while i != j:
                while i < j and distance(j) >= pivot:
                    j -= 1
                while i < j and distance(i) <= pivot:
                    i += 1
                if i < j:
                    # 交换值
                    points[i], points[j] = points[j], points[i] 
                
            # 交换哨兵
            points[i], points[oi] = points[oi], points[i]
            
            # 递归
            if K <= i - oi + 1:
                # 左半边排序
                helper(oi, i - 1, K)
            else:
                # 右半边排序
                helper(i + 1, oj, K - (i - oi + 1))
                
        helper(0, len(points) - 1, K)
        return points[:K]

        # M3. 最小堆 O(nlgk)
        import heapq
        dis = []
        for p in points:
            d = p[0] ** 2 + p[1] ** 2
            dis.append((d, p))
        heapq.heapify(dis)
        return [d[1] for d in heapq.nsmallest(K, dis)]
