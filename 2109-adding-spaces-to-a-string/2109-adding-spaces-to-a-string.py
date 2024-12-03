class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
      res = []
      s_idx = 0
      for i,c in enumerate(s):
        if s_idx < len(spaces) and i == spaces[s_idx]:
          res.append(' ')
          s_idx += 1
        res.append(c)
      return ''.join(res)  