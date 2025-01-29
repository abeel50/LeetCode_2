class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()
        def dfs(node, d1, d2):
            visited.add(node)
            for ne in graph[node]:
                if ne in visited or node in [d1, d2] and ne in [d1, d2]:
                    continue
                dfs(ne, d1, d2)
        
        n = len(edges)
        for a, b in reversed(edges):
            visited = set()
            dfs(1, a, b)
            if len(visited) == n:
                return[a,b]
