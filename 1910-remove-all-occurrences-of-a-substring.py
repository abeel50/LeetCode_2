class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        st = []
        l = len(part)
        for c in s:
            st.append(c)
            while len(st) >= l  and ''.join(st[len(st)-l:]) == part:
                st = st[:len(st)-l]
        return ''.join(st)        
