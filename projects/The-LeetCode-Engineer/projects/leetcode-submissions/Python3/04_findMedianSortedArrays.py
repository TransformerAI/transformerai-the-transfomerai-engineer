from typing import List

from utils_code.test import assertEq

class Solution:
    """
    Given two sorted arrays nums1 and nums2 of size m and n 
    respectively, return the median of the two sorted arrays.

    The overall run time complexity should be O(log (m+n)).
    """
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2
        
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2
            
            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")
            
            if Aleft <= Bright and Bleft <= Bright:
                if total % 2:
                    return min(Aright, Bright)
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1
            else:
                l = i + 1
     
if __name__ == "__main__":
    sol = Solution()
    
    # Explanation: merged array = [1,2,3] and median is 2.
    nums1 = [1,3]
    nums2 = [2]
    output = 2.00000
    assertEq([nums1, nums2], output, sol.findMedianSortedArrays(nums1, nums2))

    # Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.    
    nums1 = [1,2]
    nums2 = [3,4]
    output = 2.50000
    assertEq([nums1, nums2], output, sol.findMedianSortedArrays(nums1, nums2))