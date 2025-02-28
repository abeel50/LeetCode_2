class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)
        prv = [str2[j:] for j in range(M)]
        prv.append("")

        for i in reversed(range(N)):
            cur = [""] * M
            cur.append(str1[i:])
            for j in reversed(range(M)):
                if str1[i] == str2[j]:
                    cur[j] = str1[i] + prv[j+1] #daignoal
                else:
                    st1 = str1[i] + prv[j] #down
                    st2 = str2[j] + cur[j+1] #right
                    cur[j] = st1 if len(st1) < len(st2) else st2
            prv = cur
        return cur[0]
        
