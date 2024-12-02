from typing import List
class Solution:
    """_summary_
    Given an array nums containing n distinct numbers in the 
    range [0, n], return the only number in the range that 
    is missing from the array.

    """
    def missingNumber(self, nums: List[int]) -> int:
        if nums[-1] != len(nums):
            return len(nums)
        
        arr = [False] * len(nums)
        nums.sort()
        for n in range(len(nums)):
            if n == nums[n]:
                arr[n] = True
            else: 
                return n
        

 
if __name__ == "__main__":
    sol = Solution()
    nums = [3,0,1]
    output = 2
    out = sol.missingNumber(nums)
    print(out)
    
    nums = [0,1]
    output = 2
    out = sol.missingNumber(nums)
    print(out)
    
    nums = [9,6,4,2,3,5,7,0,1]
    output = 8
    out = sol.missingNumber(nums)
    print(out)
