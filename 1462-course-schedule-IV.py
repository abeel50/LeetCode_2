class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph =  defaultdict(list)
        for a, b in prerequisites:
            graph[b].append(a)
        
        preReqMap = {}

        def dfs(c):
            if c not in preReqMap:
                preReqMap[c] = set()
                for pre in graph[c]:
                    preReqMap[c] |= dfs(pre)
                preReqMap[c].add(c)
            return preReqMap[c]

        for course in range(numCourses):
            dfs(course)
  
        res = []
        for u,v in queries:
            res.append(u in preReqMap[v])
        return res
  
