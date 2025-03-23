class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        # Build Graph
        graph = defaultdict(list)
        for u,v,w in roads:
            graph[u].append((w,v))
            graph[v].append((w,u))
        
        minHeap = [(0,0)] #Cost, node
        minCost = [float("inf")] * n
        pathCount = [0] * n
        pathCount[0] = 1
        
        while minHeap:
            cost, node = heappop(minHeap)
            for neCost, nei in graph[node]:
                newCost = neCost + cost
                if newCost < minCost[nei]:
                    minCost[nei] = newCost
                    pathCount[nei] = pathCount[node]
                    heappush(minHeap, (newCost, nei))
                elif newCost == minCost[nei]:
                    pathCount[nei] = (pathCount[nei] + pathCount[node]) % MOD
        return pathCount[n-1] 
