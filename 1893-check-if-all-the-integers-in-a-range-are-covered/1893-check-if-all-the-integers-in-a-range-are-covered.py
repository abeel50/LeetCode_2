class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
      for n in range(left, right + 1):
        flag = False
        for start, end in ranges:
          if n >= start and n <= end:
            flag = True
        if not flag:
          return False
          
      return True