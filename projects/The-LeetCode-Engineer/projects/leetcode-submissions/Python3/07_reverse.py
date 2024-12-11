import math
from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given a signed 32-bit integer x, return x with its digits 
    reversed. If reversing x causes the value to go outside the 
    signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit 
    integers (signed or unsigned).
    """
    def reverse(self, x: int) -> int:
        MIN = -2147483648
        MAX = 2147483647
        
        res = 0
        while x:
            digit = int(math.fmod(x, 10))
            x = int(x / 10)
            if (res > MAX // 10 or (res == MAX // 10 and digit >= MAX % 10)):
                return 0
            if (res < MIN // 10 or (res == MIN // 10 and digit <= MIN % 10)):
                return 0
            res = (res * 10) + digit
        return res
    
    
if __name__ == '__main__':
    sol = Solution()
    
    x = 123
    output = 321
    assertEq(x, output, sol.reverse(x))

    x = -123
    output = -321
    assertEq(x, output, sol.reverse(x))
    
    x = 120
    output = 21
    assertEq(x, output, sol.reverse(x))