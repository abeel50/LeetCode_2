class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        # right, left, down, up
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        # Priority queue to store (cost, row, col)
        min_heap = [(0, 0, 0)]
        visited = set()

        while min_heap:
            cost, r, c = heappop(min_heap)
            if (r, c) in visited:
                continue
            visited.add((r, c))

            # If we reach the bottom-right corner, return the cost
            if r == ROWS - 1 and c == COLS - 1:
                return cost

            for i, (dr, dc) in enumerate(DIRECTIONS):
                nr, nc = r + dr, c + dc
                if isValid(nr, nc) and (nr, nc) not in visited:
                    new_cost = cost + (1 if grid[r][c] != i + 1 else 0)
                    heappush(min_heap, (new_cost, nr, nc))
        
        return -1 
