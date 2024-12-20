from typing import List

from utils_code.test import assertEq

class Solution():
    """
    You are given an array of logs. Each log is a space-delimited 
    string of words, where the first word is the identifier.

    There are two types of logs:

    Letter-logs: All words (except the identifier) consist of 
                 lowercase English letters.
    Digit-logs: All words (except the identifier) consist of 
                digits.
    Reorder these logs so that:

       - The letter-logs come before all digit-logs.
    
       - The letter-logs are sorted lexicographically by their 
         contents. If their contents are the same, then sort them 
         lexicographically by their identifiers.
       - The digit-logs maintain their relative ordering.
    
    Return the final order of the logs.
    """
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        pass
    
    
if __name__ == "__main__":
    sol = Solution()

    logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
    output = ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
    assertEq(logs, output, sol.reorderLogFiles(logs))
    
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    output = ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
    assertEq(logs, output, sol.reorderLogFiles(logs))