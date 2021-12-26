class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        non_primes = set()
        for p in range(2, int(sqrt(n)) + 1):
            if p not in non_primes:
                for multiple in range(p*p, n, p):
                    non_primes.add(multiple)
        
        # Exclude "1" and the number "n" itself.
        return n - len(non_primes) - 2
