class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        start, end = 0, 0
        
        for n in derived:
            if n:
                end = ~ end
        return start == end
