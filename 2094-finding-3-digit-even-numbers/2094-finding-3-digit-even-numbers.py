class Solution:
    def countDigits(self, digits) -> defaultdict:
        h = defaultdict(int)
        for d in digits:
            h[int(d)] += 1
        return h

    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        h = self.countDigits(digits)
        res = []
        
        for n in range(100, 1000, 2):
            num_str = str(n)
            num_h = self.countDigits(num_str)
            
            flag = True
            for d in num_h:
                if num_h[d] > h[d]:
                    flag = False
                    break
            
            if flag:
                res.append(n)
                
        return res
