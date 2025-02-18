class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res, st = [], []

        for i in range(len(s) + 1):
            st.append(i)
            while st and (i == len(s) or s[i] == 'I'):
                res.append(st.pop())
        return res
