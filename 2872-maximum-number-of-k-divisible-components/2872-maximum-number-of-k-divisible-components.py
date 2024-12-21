class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:    
      tree= defaultdict(list)
      for a, b in edges:
        tree[a].append(b)
        tree[b].append(a)
      
      visited = set()
      res = 0
      
      def dfs(node):
        v = values[node]
        visited.add(node)

        for child in tree[node]:
            if child not in visited:
                v += dfs(child)                
          
        nonlocal res 
        if v % k == 0:
          res += 1
        return v
      
      
      dfs(0)
      return res    