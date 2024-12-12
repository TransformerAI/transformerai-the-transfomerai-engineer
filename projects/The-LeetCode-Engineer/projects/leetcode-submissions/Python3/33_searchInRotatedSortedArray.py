from typing import List

from utils_code.test import assertEq

class Solution():
    """
    There is an integer array nums sorted in ascending order
    (with distinct values).

    Prior to being passed to your function, nums is possibly 
    rotated at an unknown pivot index k (1 <= k < nums.length) 
    such that the resulting array is [nums[k], nums[k+1], ..., 
    nums[n-1], nums[0], nums[1], ..., 
    nums[k-1]] (0-indexed). 
    
    For example, [0,1,2,4,5,6,7] might be rotated at pivot 
    index 3 and become [4,5,6,7,0,1,2].

    Given the array nums after the possible rotation and an 
    integer target, return the index of target if it is in nums, 
    or -1 if it is not in nums.

    You must write an algorithm with O(log n) runtime complexity.
    """
    def search(self, nums: List[int], target: int) -> int:
        pass
    
if __name__ == '__main__':
    sol = Solution()
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    output: 4
    assertEq(nums, output, sol.search(nums, target))

    nums = [4,5,6,7,0,1,2]
    target = 3
    output = -1
    assertEq(nums, output, sol.search(nums, target))
    
    nums = [1]
    target = 0
    output = -1
    assertEq(nums, output, sol.search(nums, target))
 