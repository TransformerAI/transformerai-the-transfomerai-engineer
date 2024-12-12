from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given an array of intervals where 
    intervals[i] = [starti, endi], 
    
    merge all overlapping intervals, and return an array of 
    the non-overlapping intervals that cover all the intervals 
    in the input.
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        pass
    
if __name__ == '__main__':
    sol = Solution()
    
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    output = [[1,6],[8,10],[15,18]]
    assertEq(intervals, output, sol.merge(intervals))

    intervals = [[1,4],[4,5]]
    output = [[1,5]]
    assertEq(intervals, output, sol.merge(intervals))
