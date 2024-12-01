class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        d = defaultdict(int)
        for i in range(len(arr)):
            d[i] = arr[i]
        
        values = list(d.values())
        for i in range(len(arr)):
            if 2 * d[i] in values[:i] or (arr[i]% 2== 0 and arr[i] / 2 in values[:i]):
                return True
        return False
        