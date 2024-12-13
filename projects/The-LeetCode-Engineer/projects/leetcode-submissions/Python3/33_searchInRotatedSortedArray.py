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
        # print(f"search, nums: {nums}")
        # l, r = 0, len(nums) - 1
        # while l <= r:
        #     mid = (l + r) // 2
        #     if target == nums[mid]:
        #         return mid
            
        #     if nums[l] <= nums[mid]:
        #         if target > nums[mid] or target < nums[l]:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     else:
        #         if target < nums[mid] or target > nums[r]:
        #             r = mid - 1
        #         elif target > nums[r]:
        #             l = mid + 1
        # return -1
                 
        n = len(nums)
        left, right = 0, n - 1

        # Find the index of the pivot element (the smallest element)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > nums[-1]:
                left = mid + 1
            else:
                right = mid - 1

        # Binary search over an inclusive range [left_boundary ~ right_boundary]
        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        # Binary search over elements on the pivot element's left
        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        # Binary search over elements on the pivot element's right
        return binarySearch(left, n - 1, target)
                 
if __name__ == '__main__':
    sol = Solution()
    
    nums = [4,5,6,7,0,1,2]
    target = 0
    output = 4
    assertEq(nums, output, sol.search(nums, target))

    nums = [4,5,6,7,0,1,2]
    target = 3
    output = -1
    assertEq(nums, output, sol.search(nums, target))
    
    nums = [1]
    target = 0
    output = -1
    assertEq(nums, output, sol.search(nums, target))
    
    nums = [5,1,3]
    target = 2
    