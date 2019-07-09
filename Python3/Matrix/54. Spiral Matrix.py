# Given a matrix of m x n elements (m rows, n columns), 
# return all elements of the matrix in spiral order.

# Example 1:
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solution:
    def walk_right(self, m, c, matrix, array):
        d = 0
        while d < m:
            if matrix[c][d] != '.':
                array.append(matrix[c][d])
                matrix[c][d] = '.'
            d += 1
            
    def walk_down(self, n, r, matrix, array):
        d = 0
        while d < n:
            if matrix[d][r] != '.':
                array.append(matrix[d][r])
                matrix[d][r] = '.'
            d += 1
            
    def walk_left(self, m, c, matrix, array):
        d = m-1
        while d >= 0:
            if matrix[c][d] != '.':
                array.append(matrix[c][d])
                matrix[c][d] = '.'
            d -= 1
            
    def walk_up(self, n, r, matrix, array):
        d = n-1
        while d >= 0 :
            if matrix[d][r] != '.':
                array.append(matrix[d][r])
                matrix[d][r] = '.'
            d -= 1
            
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0:
            return []
        if len(matrix) == 1:
            return matrix[0]
        
        array = []
        m = len(matrix[0])
        n = len(matrix)
        b = 0
        t = n - 1
        l = 0
        r = m - 1
        
        while(len(array) < m*n):
            if b < n:
                self.walk_right(m, b, matrix, array)
                b += 1
            
            if r >= 0:
                self.walk_down(n, r, matrix, array)
                r -= 1
            
            if t >= 0:
                self.walk_left(m, t, matrix, array)
                t -= 1
            
            if l < m:
                self.walk_up(n, l, matrix, array)
                l += 1
        return array
         