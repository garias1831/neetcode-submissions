class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        # Look at video to see his solution and implementation
        # But the idea is simple: make recursive call, at each node
        # check each number and try subtracting it from our current target
        # because nums[i] > 0, we can keep trying this and keeping track of the current
        # combination as long as we add numbers that stay below the target.
        # if target < 0 at any point, we return False,
        # and if we exactly hit the target, we prop it up to signal 
        # a valid path

        res = []

        def dfs(i, cur, total):
            if total == target:
                res.append(cur.copy())
                return
            
            if i >= len(nums) or total > target:
                return
            
            # 2 options: INCLUDE the current number in the candidate sol,
            # or move on to try and consider hte next number
            cur.append(nums[i])
            dfs(i, cur, total + nums[i])

            cur.pop()
            dfs(i + 1, cur, total)
        
        dfs(0, [], 0)

    
        return res

        