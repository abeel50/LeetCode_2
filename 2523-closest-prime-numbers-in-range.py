class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def sieveOfEratosthenes(l, r):
            prime = [True for i in range(r + 1)]
            p = 2
            while (p * p <= r):
                if (prime[p]):
                    for i in range(p * p, r + 1, p):
                        prime[i] = False
                p += 1
            
            return [p for p in range(max(l, 2), r + 1) if prime[p]]
                    
        primes = sieveOfEratosthenes(left, right)
        res = [-1, -1]
        diff = right
        for i in range(1, len(primes)):
            if primes[i] - primes[i-1] < diff:
                diff = min(diff, primes[i] - primes[i-1])
                res = [primes[i-1], primes[i]]
        return res
