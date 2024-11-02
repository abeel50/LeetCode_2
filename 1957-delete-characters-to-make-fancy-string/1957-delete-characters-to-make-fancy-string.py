class Solution:
    def makeFancyString(self, s: str) -> str:
      res = []
      curr = None
      count = 0
      for i,c in enumerate(s):
        if c == curr:
          count += 1
        else:
          curr = c
          count = 1
        if count == 3:
          count -= 1
          continue
        res.append(c)
        
      return ''.join(res)
        
        