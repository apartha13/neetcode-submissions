class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 1:
            return 0
        elif len(stones) < 2:
            return stones[0]
        
        heap = []
        
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)

            newStone = y - x
            if newStone:
                heapq.heappush(heap, newStone)
            
        return -heap[0] if heap else 0
        