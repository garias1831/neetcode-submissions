class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Cache to store previous results
        # Key: (i : int, True if we're robbing house i, False o.w)
        # Value: max profit from performing specified action at house i
        cache = dict()

        def helper(i: int, robbing: bool):
            if (i >= len(nums) - 1):
                if robbing:
                    return nums[-1]
                else:
                    return 0
            
            if (i, robbing) in cache:
                return cache[(i, robbing)]
            
            if robbing:
                profit = nums[i] + helper(i + 1, False)
                cache[(i, robbing)] = profit
                return profit
            else:
                profit = max(
                    helper(i + 1, True),
                    helper(i + 1, False)
                )
                cache[(i, robbing)] = profit
                return profit

        return max(helper(0, True), helper(0, False))
            


        

