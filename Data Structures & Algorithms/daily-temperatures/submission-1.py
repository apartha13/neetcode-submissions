class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        n = len(temperatures)
        for i in range(n - 1):
            r = i + 1
            while r < n and temperatures[i] >= temperatures[r]:
                r += 1
            if r < n:
                res.append(r - i)
            else:
                res.append(0)
        res.append(0)
        return res
