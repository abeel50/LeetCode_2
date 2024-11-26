class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
      isWeaker = [False] * n
      
      for s, w  in edges:
        isWeaker[w] = True
      
      res = -1
      c = 0
      
      for (i,t) in enumerate(isWeaker):
        if not t:
          c += 1
          res = i
        if c > 1:
          return -1
      return res
          
        
      
      
      
      
      
        