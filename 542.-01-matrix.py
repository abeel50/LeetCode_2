class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        # right, left, down, up
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def isValid(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        q = deque()
        for r in range(ROWS):
            for c in range(COLS):
                if mat[r][c] == 0:
                    q.append((r, c))
                else:
                    mat[r][c] = -1 #it's not visited
        while q:
            r, c = q.popleft()
            value = mat[r][c]
            if value == -1:
                value = 0
            
            for dr, dc in directions:
                nr, nc = r + dr , c + dc
                if not isValid(nr, nc) or mat[nr][nc] != -1:
                    continue
                q.append((nr, nc))
                mat[nr][nc] = value + 1
        return mat
        
