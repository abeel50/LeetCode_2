class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        def helperK():
            abc = defaultdict(int)
            res, l = 0, 0
            for r in range(len(s)):
                abc[s[r]] += 1
                while len(abc) >=3:
                    res += (len(s) - r)
                    abc[s[l]] -= 1
                    if abc[s[l]] == 0:
                        abc.pop(s[l])
                    l += 1
            return res
        return helperK()
