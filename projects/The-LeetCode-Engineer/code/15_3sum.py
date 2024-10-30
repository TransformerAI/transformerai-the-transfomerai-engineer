
from typing import List
import pprint

# Given an integer array nums, return all the triplets 
# 
# [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k,
# and nums[i] + nums[j] + nums[k] == 0.
# 
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# 
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# 
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
#
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        nums_length = len(nums)
        i = 0
        j = 0
        k = 0
        while i < nums_length:
            j = 0
            while j < nums_length:
                if j == i:
                    j += 1
                    continue 
                k = 0
                while k < nums_length: 
                    if k == j or k == i:
                        k += 1
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        maybe_res = [nums[i], nums[j], nums[k]]
                        maybe_res.sort()
                        if not maybe_res in res:
                            res.append(maybe_res)
                    k += 1
                j += 1
            i += 1
        return res
    
if __name__ == "__main__": 
    s = Solution()
    result = s.threeSum([-1,0,1,2,-1,-4])
    pprint.pprint(result)
        