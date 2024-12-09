from typing import List

from utils_code.test import assertEq

class Solution:
    """_summary_
    Given an integer array nums, return an array answer such that 
    answer[i] is equal to the product of all the elements of nums 
    except nums[i].

    The product of any prefix or suffix of nums is guaranteed to 
    fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without 
    using the division operation.
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = []
        for i in range(len(nums)):
            nl = list(nums)
            nl.pop(i)
            a = 1
            for n in nl: 
                a *= n
            answer.append(a)
        return answer
    
if __name__ == "__main__":
    sol = Solution()

    nums = [1,2,3,4]
    output = [24,12,8,6]
    out = sol.productExceptSelf(nums)
    print(out)
    
    nums = [-1,1,0,-3,3]
    output = [0,0,9,0,0]
    out = sol.productExceptSelf(nums)
    print(out)