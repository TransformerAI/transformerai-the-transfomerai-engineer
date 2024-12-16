from typing import List

from utils_code.test import assertEq

class Solution:
    """
    Given an integer array nums, find the subarray with the 
    largest sum, and return its sum.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        curSum = 0
        for n in nums:
            if curSum < 0:
                curSum = 0
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub
    
if __name__ == '__main__':
    sol = Solution()

    nums = [-2,1,-3,4,-1,2,1,-5,4]
    output = 6
    assertEq(nums, output, sol.maxSubArray(nums))
    
    nums = [1]
    output = 1
    assertEq(nums, output, sol.maxSubArray(nums))
    
    nums = [5,4,-1,7,8]
    output = 23
    assertEq(nums, output, sol.maxSubArray(nums))
    