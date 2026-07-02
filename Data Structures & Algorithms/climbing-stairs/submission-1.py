class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        return self.memoization(n, cache)

    def memoization(self, n, cache) -> int:
        if n <= 1:
            return 1
        if n in cache:
            return cache[n]
        
        cache[n] = self.memoization(n - 1, cache) + self.memoization(n - 2, cache)

        return cache[n]