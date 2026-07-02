import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            secLarge = heapq.heappop(stones)
            
            print(largest, secLarge, len(stones))
            if secLarge > largest:
                newWeight = largest - secLarge
                heapq.heappush(stones, newWeight)

        if stones:
            return abs(stones[0])
        else:
            return 0
        
            
            



