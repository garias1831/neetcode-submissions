class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = [-1] * (len(nums) - k + 1)

        freq = {} # Frequency count of all chars in the window
        pq = [] # To get the max in logn
        heapq.heapify(pq)

        # Main case
        l = 0
        for r in range(len(nums)):
            # Grow the window
            v = nums[r]
            freq[v] = 1 + freq.get(v, 0)
            heapq.heappush(pq, -v) # max heap trick

            # Shrink if too large
            if r - l + 1 > k:
                freq[nums[l]] -= 1
                if freq[nums[l]] == 0:
                    freq.pop(nums[l])
                l += 1

            # Compute answer
            # Max is just the top of the max heap
            # Lazily pop off maxes not in the current window
            cmax = -1
            while True:
                cmax = -1 * heapq.heappop(pq)
                if (cmax in freq):
                    heapq.heappush(pq, -cmax)
                    break
        
            if r >= k - 1:
                res[r - k + 1] = cmax            
        
        return res
            




        