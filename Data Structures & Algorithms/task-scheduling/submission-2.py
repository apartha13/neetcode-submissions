class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        wait_q = deque()
        heap = []
        time = 0

        count = Counter(tasks)

        for task, freq in count.items():
            heapq.heappush(heap, -freq)

        while heap or wait_q:
            time += 1
            if heap:
                freq = 1 + heapq.heappop(heap)
                if freq:
                    wait_q.append((freq, time + n))
            while wait_q and wait_q[0][1] <= time:
                heapq.heappush(heap, wait_q.popleft()[0])
        
        return time