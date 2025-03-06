class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        SIZE = len(grid)
        sm = 0
        hash = defaultdict(int)
        res = []
        for r in range(SIZE):
            for c in range(SIZE):
                n = grid[r][c]
                sm += n
                hash[n] += 1
                if (hash[n]) == 2:
                    res.append(n)
        SIZE *= SIZE
        res.append(((SIZE * (SIZE + 1)) // 2) - (sm - res[0]))
        return res       
