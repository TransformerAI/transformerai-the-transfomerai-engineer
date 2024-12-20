from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given an array of integers nums and an integer target, return
    indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one 
    solution, and you may not use the same element twice.

    You can return the answer in any order.
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

if __name__ == "__main__":
    sol = Solution()
    
    nums = [2,7,11,15]
    target = 9
    output = [0,1]
    assertEq(nums, output, sol.twoSum(nums, target))

    nums = [3,2,4]
    target = 6
    output = [1,2]
    assertEq(nums, output, sol.twoSum(nums, target))
    
    nums = [3,3]
    target = 6
    output = [0,1]
    assertEq(nums, output, sol.twoSum(nums, target))
    
