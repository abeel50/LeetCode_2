class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        ngt = 0
        minNgt = float('inf')
        for row in matrix:
          for e in row:
            if e < 0:
              ngt += 1
            minNgt = min(minNgt, abs(e))
            res += abs(e)
        
        if ngt % 2 == 0:
          return res
        
        return res - (2 *minNgt) 
              