import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # Create an empty min heap
        heap = []

        # Traverse every element in the array
        for i in nums:

            # Push the current element into the min heap
            heapq.heappush(heap, i)

            # If the heap size becomes greater than k,
            # remove the smallest element
            # This ensures that the heap always contains
            # only the k largest elements seen so far.
            if len(heap) > k:
                heapq.heappop(heap)

        # The root of the min heap is the smallest among
        # the k largest elements, which is exactly the
        # kth largest element in the array.
        return heap[0]