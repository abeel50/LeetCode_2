class Solution:
    def punishmentNumber(self, n: int) -> int:
        def isPartition(i, cur, target, string):
            if i == len(string) and cur == target:
                return True
            
            for j in range(i, len(string)):
                if isPartition(j + 1, cur + int(string[i: j+1]), target, string):
                    return True
            return False

        res = 0
        for i in range(1, n + 1):
            if isPartition(0, 0, i, str(i * i)):
                res += i * i
        return res
        
