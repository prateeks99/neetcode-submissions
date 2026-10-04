class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        minheap = []
        for n in count.keys():
            heapq.heappush(minheap, (count[n],n))
            if len(minheap) > k:
                heapq.heappop(minheap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(minheap)[1])
        return res

