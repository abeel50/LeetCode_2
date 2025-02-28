class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        cache = {}
        def backTrack(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            
            if i == len(str1):
                return str2[j:]
            if j == len(str2):
                return str1[i:]

            if str1[i] == str2[j]:
                return str1[i] + backTrack(i + 1, j + 1)
            
            st1 = str1[i] + backTrack(i + 1, j)
            st2 = str2[j] + backTrack(i, j + 1)
            cache[(i, j)] = st1 if len(st1) <= len(st2) else st2
            return cache[(i, j)]

        return backTrack(0, 0)
