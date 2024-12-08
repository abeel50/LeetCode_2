class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
      events.sort()
      curr = float('-inf')
      res = max(v for _, _, v in events)
      hp = [] #heap
      for s,e,v in events:
        while len(hp) > 0 and hp[0][0] <= s:
          _, nv = heapq.heappop(hp)
          curr = max(curr, nv)
        heapq.heappush(hp, (e + 1, v))
        res = max(res, curr + v)
      return res