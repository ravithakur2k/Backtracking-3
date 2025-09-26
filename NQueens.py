# Time Complexity : O(N!) because for each row there are n-1, n-2, n-3 options, hence total would be n factorial
# Space Complexity : O(n^2)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# The intuition here is to create a boolean grid with n*n. Then try the exhaustive way to put Queens in each row
# But before putting check if its a safe place to put by check upper rows, upper left row and col and upper right row and col

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        grid = [[False for _ in range(n)] for _ in range(n)]
        result = []

        def backtrack(r, n):
            # Base case
            if r == n:
                list_ = []
                for i in range(n):
                    subResult = []
                    for j in range(n):
                        if grid[i][j] == True:
                            subResult.append("Q")
                        else:
                            subResult.append(".")
                    list_.append("".join(subResult))
                result.append(list_)
                return

            # logic
            for i in range(n):
                if isSafe(r, i):
                    grid[r][i] = True
                    backtrack(r + 1, n)
                    grid[r][i] = False

        def isSafe(r, c):
            for i in range(r):
                if grid[i][c]:
                    return False
            i, j = r, c
            while i >= 0 and j >= 0:
                if grid[i][j] == True:
                    return False
                i -= 1
                j -= 1

            i, j = r, c
            while i >= 0 and j < n:
                if grid[i][j] == True:
                    return False
                i -= 1
                j += 1
            return True

        backtrack(0, n)

        return result