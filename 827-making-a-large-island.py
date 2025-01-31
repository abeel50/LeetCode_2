class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Step 1: Create a unique ID for each island and store its size using BFS
        def bfs(r, c, island_id):
            queue = deque([(r, c)])
            visited.add((r, c))
            island_map[r, c] = island_id
            size = 1
            
            while queue:
                curr_r, curr_c = queue.popleft()
                
                for dr, dc in DIRECTIONS:
                    nr, nc = curr_r + dr, curr_c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and 
                        grid[nr][nc] == 1 and (nr, nc) not in visited):
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        island_map[nr, nc] = island_id
                        size += 1
            
            return size
        
        # Step 2: Map each cell to its island ID and compute island sizes
        visited = set()
        island_map = {}     # (r, c) -> island_id
        island_sizes = {}   # island_id -> size
        island_id = 2       # Start from 2 to avoid confusion with 0s and 1s
        
        # Find all islands using BFS
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in visited:
                    island_sizes[island_id] = bfs(r, c, island_id)
                    island_id += 1
        
        # If the grid is all 1s, return the total size
        if len(visited) == ROWS * COLS:
            return ROWS * COLS
        
        # Step 3: For each 0, check the size if we convert it to 1
        max_size = max(island_sizes.values(), default=0)
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    # Get neighboring island IDs
                    neighbor_islands = set()
                    for dr, dc in DIRECTIONS:
                        nr, nc = r + dr, c + dc
                        if (0 <= nr < ROWS and 0 <= nc < COLS and 
                            (nr, nc) in island_map):
                            neighbor_islands.add(island_map[nr, nc])
                    
                    # Calculate size if we convert this 0 to 1
                    current_size = 1  # Start with 1 for the current cell
                    for island_id in neighbor_islands:
                        current_size += island_sizes[island_id]
                    
                    max_size = max(max_size, current_size)
        
        return max_size
