class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballsHash = defaultdict(int)
        colorHash = defaultdict(set)
        res = []
        for b, c in queries:
            if ballsHash[b] > 0:
                prvColor = ballsHash[b]
                colorHash[prvColor].remove(b)
                if not len(colorHash[prvColor]):
                    del colorHash[prvColor]
            ballsHash[b] = c
            colorHash[c].add(b)
            res.append(len(colorHash))
        return res    
