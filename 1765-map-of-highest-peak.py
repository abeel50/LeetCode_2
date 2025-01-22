class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(isWater), len(isWater[0])
        # right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if isWater[r][c]:
                    isWater[r][c] = 0
                    q.append((r, c))
                else:
                    isWater[r][c] = -1 #it's Land not visited
        while q:
            r, c = q.popleft()
            value = isWater[r][c]
            if value == -1:
                value = 0
            
            for dr, dc in directions:
                nr, nc = r + dr , c + dc
                if not isValid(nr, nc) or isWater[nr][nc] != -1:
                    continue
                q.append((nr, nc))
                isWater[nr][nc] = value + 1
        return isWater
        
