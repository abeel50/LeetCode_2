class Solution:
    def minimumLength(self, s: str) -> int:
        count = {c: s.count(c) for c in set(s)}
        res = 0
        for k,v in count.items():
            if v % 2:
                res += 1
            else:
                res += 2
        return res        
