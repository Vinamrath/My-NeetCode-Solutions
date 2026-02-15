class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
          # Count the frequency of each element
        freq_map = Counter(nums)
        
        # Use a min-heap to store the k most frequent elements
        heap = []
        for num, freq in freq_map.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Extract elements from the heap
        return [num for freq, num in heap]