from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given an m x n matrix, return all elements of the matrix
    in spiral order.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        left = 0 
        right = len(matrix[0])
        top = 0
        bottom = len(matrix)
        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1
            
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1
            if not (left < right and top < bottom):
                break
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1
        return res
    
if __name__ == '__main__':
    sol = Solution()
    
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    output = [1,2,3,6,9,8,7,4,5]
    assertEq(matrix, output, sol.spiralOrder(matrix))

    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    output = [1,2,3,4,8,12,11,10,9,5,6,7]
    assertEq(matrix, output, sol.spiralOrder(matrix))