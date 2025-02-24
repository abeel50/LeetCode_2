class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 1: Find Bob's path to node 0 using DFS
        parent = {0: None}
        def dfs_bob(node, par):
            parent[node] = par
            for adj in graph[node]:
                if adj != par:
                    dfs_bob(adj, node)
        
        dfs_bob(0, None)  # Establish parent-child relationships
        
        # Step 2: Compute the time Bob reaches each node
        bobTimeVal = {}
        time = 0
        curr = bob
        while curr is not None:
            bobTimeVal[curr] = time
            curr = parent[curr]
            time += 1
        
        # Step 3: Alice's DFS traversal
        visited = set()
        def dfs_alice(node, time):
            if node in bobTimeVal:
                if bobTimeVal[node] > time:
                    profit = amount[node]  # Alice reaches first
                elif bobTimeVal[node] == time:
                    profit = amount[node] // 2  # Both arrive at the same time
                else:
                    profit = 0  # Bob arrives first
            else:
                profit = amount[node]

            visited.add(node)
            max_profit = float('-inf')
            is_leaf = True
            for adj in graph[node]:
                if adj not in visited:
                    is_leaf = False
                    max_profit = max(max_profit, dfs_alice(adj, time + 1))
            
            return profit if is_leaf else profit + max_profit  # Ensure leaves contribute properly

        return dfs_alice(0, 0)
