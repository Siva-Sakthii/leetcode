import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        pq = []
        heapq.heapify(pq)
        ans,j = 0,0

        max_day = max(events[i][1] for i in range(n))
        events.sort()

        for i in range(1, max_day+1):
            while j<n and events[j][0]<=i:
                heapq.heappush(pq,events[j][1])
                j+=1
            while pq and pq[0]<i:
                heapq.heappop(pq)
            if pq:
                heapq.heappop(pq)
                ans+=1
        return ans