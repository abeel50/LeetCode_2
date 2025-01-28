class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        #Vlidate Fuction
        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS and grid[r][c] > 0
        # right, left, down, up
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            fishes = grid[r][c]
            grid[r][c] = 0
            for dr, dc in DIRECTIONS:
                nr, nc = r + dr, c + dc
                if isValid(nr, nc):
                    fishes += dfs(nr, nc)
            return fishes
            
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] > 0:
                    res = max(res, dfs(r, c))
        return res
