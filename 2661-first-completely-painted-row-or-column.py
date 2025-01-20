class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        ROWS, COLS = len(mat), len(mat[0])
        valuePos = {}

        for r in range(ROWS):
            for c in range(COLS):
                valuePos[mat[r][c]] =(r, c)
        
        rowsFreq, colsFreq = defaultdict(int), defaultdict(int)

        for i, v in enumerate(arr):
            r,c = valuePos[v]
            rowsFreq[r] += 1
            colsFreq[c] += 1
            
            if rowsFreq[r] == COLS:
                return i
            if colsFreq[c] == ROWS:
                return i
        
