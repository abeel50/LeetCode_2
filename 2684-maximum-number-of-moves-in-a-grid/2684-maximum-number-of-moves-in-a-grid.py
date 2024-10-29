
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        MOVES = [(-1, 1), (0, 1), (1, 1)]
        cache = {}

        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            
            max_path = 0
            for dr, dc in MOVES:
                nr, nc = r + dr, c + dc
                if isValid(nr, nc) and grid[nr][nc] > grid[r][c]:
                    max_path = max(max_path, 1 + dfs(nr, nc))
            
            cache[(r, c)] = max_path
            return max_path

        # Try starting from each cell in the first column
        res = 0
        for r in range(ROWS):
            res = max(res, dfs(r, 0))

        return res
