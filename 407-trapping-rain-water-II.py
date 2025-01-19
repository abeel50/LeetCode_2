class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        ROWS, COLS = len(heightMap), len(heightMap[0])
        # right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        
        minHeap = []
        for r in range(ROWS):
            for c in range(COLS):
                if r in [0, ROWS - 1] or c in [0, COLS -1]:
                    heappush(minHeap,( heightMap[r][c], r, c))
                    heightMap[r][c] = -1 #-1 indicaties that cell has been visited already
        
        res = 0
        max_h = -1

        while minHeap:
            h, r, c  = heappop(minHeap)
            max_h = max (h, max_h)
            res += max_h - h

            for dr, dc in directions:
                nr, nc = r+ dr, c + dc
                # if Neigboring cell is valid and has not been marked visited
                if not isValid(nr, nc) or -1 == heightMap[nr][nc]:
                    continue
                heappush(minHeap,( heightMap[nr][nc], nr, nc))
                heightMap[nr][nc] = -1
        
        return res
        
