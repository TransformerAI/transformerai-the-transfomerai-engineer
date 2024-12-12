from typing import List

from utils_code.test import assertEq


class Solution:
    """
    Given an array nums containing n distinct numbers in the 
    range [0, n], return the only number in the range that 
    is missing from the array.
    """
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)
        for i in range(len(nums)):
            res += (i - nums[i])
        
        return res

 
if __name__ == "__main__":
    sol = Solution()
    
    nums = [3,0,1]
    expected = 2
    assertEq(nums, expected, sol.missingNumber(nums))
    
    nums = [0,1]
    expected = 2
    assertEq(nums, expected, sol.missingNumber(nums))
     
    nums = [9,6,4,2,3,5,7,0,1]
    expected = 8
    out = sol.missingNumber(nums)
    assertEq(nums, expected, out)    