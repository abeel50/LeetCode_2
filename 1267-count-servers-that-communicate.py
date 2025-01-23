class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        rowCount, colCount = [0] * ROWS, [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    rowCount[r] += 1
                    colCount[c] += 1
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]:
                    res += max(rowCount[r], colCount[c]) > 1
        return res
