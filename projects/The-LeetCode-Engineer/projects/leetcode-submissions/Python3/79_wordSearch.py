from typing import List

from utils_code.test import assertEq

class Solution():
    """
    Given an m x n grid of characters board and a string word, 
    return true if word exists in the grid.

    The word can be constructed from letters of sequentially 
    adjacent cells, where adjacent cells are horizontally or 
    vertically neighboring. The same letter cell may not be 
    used more than once.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        path = set()
        
        def dfs(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or (r,c) in path):
                return False
    
if __name__ == '__main__':
    sol = Solution()
    
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    output = True
    assertEq(board, output, sol.exist(board, word))

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    output = True
    assertEq(board, output, sol.exist(board, word))

    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    output = False
    assertEq(board, output, sol.exist(board, word))