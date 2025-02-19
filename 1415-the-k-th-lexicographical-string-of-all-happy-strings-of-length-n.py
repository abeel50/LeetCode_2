class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        happy = []

        def backTrack(s):
            if len(s) > n:
                return
            if len(s) == n:
                happy.append("".join(s))
                return
            for c in ['a', 'b', 'c']:
                if len(s) == 0 or s[-1] != c:
                    s.append(c)
                    backTrack(s)
                    s.pop()
                    
        backTrack([])
        happy.sort()
        if k <= len(happy):
            return happy[k-1]
        else:
            return ""        
