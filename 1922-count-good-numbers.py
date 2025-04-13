class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        
        # Helper function to calculate modular exponentiation
        def modular_pow(base, exp, mod):
            return pow(base, exp, mod)
        
        # Calculate the result using modular exponentiation
        half = n // 2
        if n % 2 == 0:
            # Even case
            return modular_pow(20, half, MOD)
        else:
            # Odd case
            return (modular_pow(4, half, MOD) * modular_pow(5, half + 1, MOD)) % MOD
