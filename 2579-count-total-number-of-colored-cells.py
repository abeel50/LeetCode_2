class Solution:
    def coloredCells(self, n: int) -> int:
        res = n * 2 - 1
        for i in range(1, (n*2)-1, 2):
            res += i * 2
        return res       
