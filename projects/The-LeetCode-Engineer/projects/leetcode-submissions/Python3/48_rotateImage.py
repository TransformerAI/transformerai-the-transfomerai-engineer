
from typing import List

from utils_code.test import assertEq

class Solution():
    """
    You are given an n x n 2D matrix representing an image, 
    rotate the image by 90 degrees (clockwise).

    You have to rotate the image in-place, which means you 
    have to modify the input 2D matrix directly. 
    DO NOT allocate another 2D matrix and do the rotation.
    """
    def rotate(self, matrix: List[List[int]]):
        left, right = 0, len(matrix) - 1
        while left < right:
            for i in range(right - left):
                top, bottom = left, right
                topLeft = matrix[top][left + i]

                matrix[top][left + i] =    matrix[bottom - i][left]
                matrix[bottom - i][left] = matrix[bottom][right - i]
                matrix[bottom][right - i] = matrix[top + i][right]
                matrix[top + i][right] =    topLeft
                
            right -= 1
            left += 1
            
            
if __name__ == "__main__":
    sol = Solution()

    matrix = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
    ]
    output = [
        [7,4,1],
        [8,5,2],
        [9,6,3]
    ]
    assertEq([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]], sol.rotate(matrix))
    
    
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    assertEq(matrix, output, sol.rotate(matrix))
    
    
    