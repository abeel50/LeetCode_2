class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        
        # Step 1: Find maximum chain lengths ending at each node
        chain_lengths = [1] * n
        indegree = [0] * n
        
        # Calculate indegree for each node
        for i in range(n):
            indegree[favorite[i]] += 1
            
        # Start with nodes having no incoming edges (indegree = 0)
        queue = []
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                
        # Calculate chain lengths using topological sort
        while queue:
            curr = queue.pop(0)
            next_node = favorite[curr]
            chain_lengths[next_node] = max(chain_lengths[next_node], chain_lengths[curr] + 1)
            indegree[next_node] -= 1
            if indegree[next_node] == 0:
                queue.append(next_node)
        
        # Step 2: Process cycles and calculate result
        visited = [False] * n
        max_cycle = 0  # For case 1: maximum cycle size
        total_pairs = 0  # For case 2: sum of pair cycles with their chains
        
        for i in range(n):
            if not visited[i]:
                cycle = []
                curr = i
                
                # Find cycle
                while not visited[curr]:
                    visited[curr] = True
                    cycle.append(curr)
                    curr = favorite[curr]
                
                if curr in cycle:
                    # Get cycle length
                    cycle_length = len(cycle) - cycle.index(curr)
                    
                    if cycle_length == 2:
                        # For mutual pairs, add their chain lengths
                        a, b = curr, favorite[curr]
                        total_pairs += chain_lengths[a] + chain_lengths[b]
                    else:
                        # For larger cycles, just use cycle length
                        max_cycle = max(max_cycle, cycle_length)
        
        # Return maximum between:
        # 1. Maximum cycle length
        # 2. Total length of pair cycles with their chains
        return max(max_cycle, total_pairs)
