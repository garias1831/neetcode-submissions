from functools import cache

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Keep -> 
        

        @cache
        def dfs(i, rob, robbed_first):
            if i >= len(nums): return 0

            print(f"i: {i}")

            # Case 1: rob on this run
            if rob:
                # If at the end, rob iff we did not rob the first house
                # o.w we're forced to skip, because we robbed the first house
                if i == len(nums) - 1:
                    return nums[i] if not robbed_first else 0
                else: # Generic rob case -> must skip the next house
                    return nums[i] + dfs(i + 1, False, robbed_first)
            
            # Case 2: don't rob this house -> means next run, we can either skip or rob next house      
            return max(
                dfs(i + 1, False, robbed_first),
                dfs(i + 1, True, robbed_first)
            )

        if len(nums) == 1: return nums[0]
        
        return max(
            dfs(0, True, True),
            dfs(0, False, False)
        )
                    
                    





        
        
        