class Solution:
    def clearDigits(self, s: str) -> str:
        st = []
        for c in s:
            if c in ['0', '1', '2', '3', '4', '5','6', '7', '8', '9']:
                st.pop()
            else:
                st.append(c)
        return ''.join(st)     
