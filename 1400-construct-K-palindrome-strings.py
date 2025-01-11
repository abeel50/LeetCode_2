class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        counts = defaultdict(int)
        for c in s:
            counts[c] += 1
        
        odd = 0
        for v in counts.values():
            odd += v % 2
            if odd > k:
                return False
        return True
