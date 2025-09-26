# Time Complexity : O(m*n.3^L) where m and n are length of the board and L is the length of the word.
# Why 3^L because we will be moving in 3 directions as we have one visited.
# Space Complexity : O(L) recursion stack
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

#The intuition here is to do a DFS from each cell of the board and traverse in horizontal and vertical directions until the word is found.
# If not found then return False. Using the # logic to mark the cell as visited

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def dfs(r, c, idx):
            # Base case
            if idx == len(word):
                return True

            if r < 0 or c < 0 or r == m or c == n or board[r][c] == "#":
                return False

            # Logic
            if board[r][c] == word[idx]:
                board[r][c] = "#"
                for dx, dy in directions:
                    nr = r + dx
                    nc = c + dy
                    if dfs(nr, nc, idx + 1):
                        return True
                board[r][c] = word[idx]

        for r in range(m):
            for c in range(n):
                if dfs(r, c, 0):
                    return True
        return False