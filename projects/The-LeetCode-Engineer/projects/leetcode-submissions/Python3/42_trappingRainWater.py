from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given n non-negative integers representing an elevation map 
    where the width of each bar is 1, compute how much water it 
    can trap after raining.
    """
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        res = 0
        
        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                res += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                res += right_max - height[r]
        return res
    
if __name__ == "__main__":
    sol = Solution()
    
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    output = 6
    assertEq(height, output, sol.trap(height))

    height = [4,2,0,3,2,5]
    output = 9
    assertEq(height, output, sol.trap(height))