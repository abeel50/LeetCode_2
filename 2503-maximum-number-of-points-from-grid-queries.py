class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        # right, left, down, up
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ROWS, COLS = len(grid), len(grid[0])

        # Validate Function
        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        # Sort queries and keep track of their original indices
        sorted_queries = sorted((query, i) for i, query in enumerate(queries))
        results = [0] * len(queries)

        # Min-heap for BFS and a set for visited cells
        min_heap = [(grid[0][0], 0, 0)]
        visited = set()
        visited.add((0, 0))
        points = 0

        # Process each query in sorted order
        for query, i in sorted_queries:
            while min_heap and min_heap[0][0] < query:
                value, r, c = heapq.heappop(min_heap)
                points += 1
                for dr, dc in DIRECTIONS:
                    nr, nc = r + dr, c + dc
                    if isValid(nr, nc) and (nr, nc) not in visited:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            results[i] = points

        return results
