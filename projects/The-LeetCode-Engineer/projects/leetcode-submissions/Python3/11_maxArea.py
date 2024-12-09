from typing import List

from utils_code.test import assertEq

class Solution:
    """_summary_
    You are given an integer array height of length n. 
    There are n vertical lines drawn such that the two 
    endpoints of the ith line are (i, 0) and (i, height[i]).

    Find two lines that together with the x-axis form a 
    container, such that the container contains the most 
    water.

    Return the maximum amount of water a container can 
    store.

    Notice that you may not slant the container.
    """
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            res = max(res, (r - l) * min(height[l], height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    
    height = [1,8,6,2,5,4,8,3,7]
    output = 49
    assertEq(height, output, sol.maxArea(height))

    height = [1,1]
    output = 1
    assertEq(height, output, sol.maxArea(height))
 