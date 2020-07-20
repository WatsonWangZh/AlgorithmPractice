# 1515. Best Position for a Service Centre
# User Accepted:659
# User Tried:1224
# Total Accepted:777
# Total Submissions:3499
# Difficulty:Hard
# A delivery company wants to build a new service centre in a new city. 
# The company knows the positions of all the customers in this city on a 2D-Map 
# and wants to build the new centre in a position 
# such that the sum of the euclidean distances to all customers is minimum.
# Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, 
# return the minimum sum of the euclidean distances to all customers.
# In other words, you need to choose the position of the service centre [xcentre, ycentre] 
# such that the following formula is minimized:
# Answers within 10^-5 of the actual value will be accepted.

# Example 1:
# Input: positions = [[0,1],[1,0],[1,2],[2,1]]
# Output: 4.00000
# Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] 
# will make the distance to each customer = 1, 
# the sum of all distances is 4 which is the minimum possible we can achieve.

# Example 2:
# Input: positions = [[1,1],[3,3]]
# Output: 2.82843
# Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843

# Example 3:
# Input: positions = [[1,1]]
# Output: 0.00000

# Example 4:
# Input: positions = [[1,1],[0,0],[2,0]]
# Output: 2.73205
# Explanation: At the first glance, you may think 
# that locating the centre at [1, 0] will achieve the minimum sum, 
# but locating it at [1, 0] will make the sum of distances = 3.
# Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
# Be careful with the precision!

# Example 5:
# Input: positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
# Output: 32.94036
# Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.
 
# Constraints:
# 1 <= positions.length <= 50
# positions[i].length == 2
# 0 <= positions[i][0], positions[i][1] <= 100

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        # 梯度下降法
        # https://leetcode-cn.com/problems/best-position-for-a-service-centre/solution/ti-du-xia-jiang-suan-fa-xiang-jie-python3-by-dz-le/

        # 初始迭代位置
        x0 = sum([p[0] for p in positions]) / len(positions)
        y0 = sum([p[1] for p in positions]) / len(positions)

        # 初始步长
        step = 16
        while True:
            dx, dy = self.deri(x0, y0, positions)
            # 导数都为0, 说明当前是极值点, 退出循环。凹函数的证明可以参考其他文章
            if (dx, dy) == (0, 0):
                break

            while True:
                x1 = x0 - step * dx
                y1 = y0 - step * dy
                # 保持x0、y0不变，一直寻找下一个下降点，并在此期间改变步长
                if self.dist(x1, y1, positions) < self.dist(x0, y0, positions):
                    break

                # 减少步长
                step /= 4

            if abs(self.dist(x1, y1, positions) - self.dist(x0, y0, positions)) < 10 ** -7:
                break

            # 转移到下一个位置点
            x0, y0 = x1, y1

        return self.dist(x0, y0, positions)

    def dist(self, x, y, positions):
        """计算欧式距离"""
        return sum([((x - xi) ** 2 + (y - yi) ** 2) ** 0.5 for xi, yi in positions])

    def deri(self, x, y, positions):
        """计算导数（偏微分）"""
        dx, dy = 0, 0
        for xi, yi in positions:
            div = ((x - xi) ** 2 + (y - yi) ** 2) ** 0.5
            if div == 0: continue
            dx += (x - xi) / div
            dy += (y - yi) / div
        return dx, dy
