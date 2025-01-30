class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        # Build adjacency list
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def bfs(start):
            # Returns maximum possible groups starting from 'start' node
            dist = [-1] * (n + 1)
            dist[start] = 0
            queue = deque([start])
            max_dist = 0
            
            while queue:
                curr = queue.popleft()
                for nei in graph[curr]:
                    if dist[nei] == -1:
                        dist[nei] = dist[curr] + 1
                        max_dist = max(max_dist, dist[nei])
                        queue.append(nei)
                    elif abs(dist[nei] - dist[curr]) != 1:
                        return -1
            return max_dist + 1
        
        # Find connected components using DFS
        def dfs(node, component):
            visited[node] = True
            component.append(node)
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei, component)
        
        visited = [False] * (n + 1)
        components = []
        for i in range(1, n + 1):
            if not visited[i]:
                component = []
                dfs(i, component)
                components.append(component)
        
        ans = 0
        # Process each component
        for component in components:
            max_groups = -1
            # Try starting from each node in the component
            for start in component:
                groups = bfs(start)
                if groups == -1:
                    return -1
                max_groups = max(max_groups, groups)
            ans += max_groups
            
        return ans
