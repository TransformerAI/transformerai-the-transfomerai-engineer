from typing import List

from utils_code.test import assertEq

class Solution:
    """
    Given an integer array nums of length n and an integer 
    target, find three integers in nums such that the sum 
    is closest to target.

    Return the sum of the three integers.

    You may assume that each input would have exactly one 
    solution.
    """
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        pass
    
    
if __name__ == "__main__":
    sol = Solution()

    nums = [-1,2,1,-4]
    target = 1
    output = 2
    assertEq(nums, output, sol.threeSumClosest(nums, target))

    nums = [0,0,0]
    target = 1
    output = 0
    assertEq(nums, output, sol.threeSumClosest(nums, target))
 