from typing import List

from utils_code.test import assertEq

class Solution:
    """
    Convert a non-negative integer num to its English words representation.
    """
    def numberToWords(self, num: int) -> str:
       pass 
        
        
 
if __name__ == "__main__":
    sol = Solution()
    
    num = 123
    expected = "One Hundred Twenty Three"
    assertEq(num, expected, sol.numberToWords(num))
    
    num = 12345
    output = "Twelve Thousand Three Hundred Forty Five"
    assertEq(num, output, sol.numberToWords(num))

    num = 1234567
    output = "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
    assertEq(num, output, sol.numberToWords(num))
