class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [math.inf] * n
        prices[src] = 0

        for _ in range(k + 1):
            tmp = prices.copy()

            for from_i, to_i, price_i in flights:
                if prices[from_i] == math.inf:
                    continue
                
                if prices[from_i] + price_i < tmp[to_i]:
                    tmp[to_i] = prices[from_i] + price_i
            
            prices = tmp
        
        if prices[dst] == math.inf:
            return -1 
            
        return prices[dst]