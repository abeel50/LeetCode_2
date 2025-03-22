class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for n1, n2 in edges:
            graph[n1].append(n2)
            graph[n2].append(n1)

        visited = set()
        def dfs(node, component):
            visited.add(node)
            component.append(node)
            for ne in graph[node]:
                if ne not in visited:
                    dfs(ne, component)
        
        res = 0
        for i in range(n):
            if i not in visited:
                component = []
                dfs(i, component)
                
                # Count total edges in this component
                edge_count = 0
                for node in component:
                    edge_count += len([ne for ne in graph[node] if ne in component])
                
                # Each edge is counted twice (once from each end)
                edge_count //= 2
                
                # Check if it's a complete component
                nodes_count = len(component)
                expected_edges = (nodes_count * (nodes_count - 1)) // 2
                
                if edge_count == expected_edges:
                    res += 1
        
        return res
