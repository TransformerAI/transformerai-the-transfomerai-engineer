
import pprint
from typing import List

class Solution():
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
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    expected = [[7,4,1],[8,5,2],[9,6,3]]
    pprint.pprint(matrix)
    s = Solution()
    s.rotate(matrix)
    pprint.pprint(matrix)
    pprint.pprint(expected)
    
    print("\n")
    
    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    expected = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
    pprint.pprint(matrix)
    s.rotate(matrix)
    pprint.pprint(matrix)
    pprint.pprint(expected)