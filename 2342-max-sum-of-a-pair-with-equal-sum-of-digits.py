class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def sum_digits(n):
            d = str(n)
            return sum(int(s) * d.count(s) for s in "123456789")
        
        hash = defaultdict(list)
        for n in nums:
            dgSum = sum_digits(n)
            hash[dgSum].append(n)
            curr = hash[dgSum]
            if len(curr) > 2:
                curr.sort()
                curr.pop(0)
            
        res = -1
        for _, v in hash.items():
            if len(v) > 1:
                res = max(res,sum(v))
        return res        
