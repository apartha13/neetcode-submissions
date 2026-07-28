class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        n = len(stones)
        if not n:
            return 0
        if n < 2:
            return stones[0]

        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        
        while len(heap) > 1:
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap, y - x)
            
        return -heap[0] if heap else 0
        