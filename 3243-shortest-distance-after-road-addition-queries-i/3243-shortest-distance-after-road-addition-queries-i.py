class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
      adj = [[i+1] for i in range(n)]
      
        
      def bfs():
        q = deque()
        q.append((0, 0)) #node, dist
        visited = set()
        visited.add(0)
        
        while q:
          node, dist = q.popleft()
          if node == n - 1:
            return dist
          for ne in adj[node]:
            if ne not in visited:
              q.append((ne, dist + 1))
              visited.add(ne)
          
      
      res =[]
      for s, d in queries:
        adj[s].append(d)
        res.append(bfs())
      
      return res