class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
      
      def getAdj(edges):
        adj = defaultdict(list)
        for a,b in edges:
          adj[a].append(b)
          adj[b].append(a)
        return adj
      
      g1 = getAdj(edges1)
      g2 = getAdj(edges2)
      
      def getDiameter(par, cur, graph):
        maxD = 0
        maxChildPaths =[0, 0]
        
        for ne in graph[cur]:
          if ne == par:
            continue
          neD , neMaxChild = getDiameter(cur,ne, graph)
          maxD = max(maxD, neD)
          heappush(maxChildPaths, neMaxChild)
          heappop(maxChildPaths)
          
        
        maxD = max(maxD, sum(maxChildPaths))
        return [maxD, 1 + max(maxChildPaths)]
      
      
      d1, _ = getDiameter(-1, 0, g1)
      d2, _ = getDiameter(-1, 0, g2)
      
      return max(d1, d2, 1 + ceil(d1/2) + ceil(d2/2))