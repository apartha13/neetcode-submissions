import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = stones[i] * (-1)
        print(stones)
        heapq.heapify(stones)
        while stones:
            x = heapq.heappop(stones)
            if stones:
                y = heapq.heappop(stones)
                if x < y:
                    heapq.heappush(stones, -(y-x))
                elif x > y:
                    heapq.heappush(stones, -(x-y))
            else:
                return -x
            print(stones)
        return 0
        
            
            



