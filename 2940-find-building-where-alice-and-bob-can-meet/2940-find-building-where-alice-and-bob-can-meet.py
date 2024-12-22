class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
      res = [-1] * len(queries)
      
      groups = defaultdict(list)
      
      for i, q in enumerate(queries):
        l, r = sorted(q)
        if l == r or heights[r] > heights[l]:
          res[i] = r
        else:
          h = max(heights[l], heights[r])
          groups[r].append((h, i))
      
      heap = []
      
      for i, h in enumerate(heights):
        
        for q_h, q_i in groups[i]:
          heapq.heappush(heap, (q_h, q_i))
          
        while heap and h > heap[0][0]:
          q_h, q_i = heapq.heappop(heap)
          res[q_i] = i
      
      return res