from typing import List

from utils_code.test import assertEq

class Solution:
    """
    Given an integer array nums, return all the triplets 
    [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
    and nums[i] + nums[j] + nums[k] == 0.

    Notice that the solution set must not contain duplicate triplets.
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
    
if __name__ == "__main__":
    sol = Solution()
    
    nums = [-1,0,1,2,-1,-4]
    output = [[-1,-1,2],[-1,0,1]]
    assertEq(nums, output, sol.threeSum(nums))
    
    nums = [0,1,1]
    output = []
    assertEq(nums, output, sol.threeSum(nums))

    nums = [0,0,0]
    output = [[0,0,0]]
    assertEq(nums, output, sol.threeSum(nums))
