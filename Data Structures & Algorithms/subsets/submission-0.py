class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res, part = [], []
        def dfs(i):
            if i >= len(nums):
                res.append(part.copy())
                return


            # choose
            part.append(nums[i])
            dfs(i + 1)

            # After recursing, we should get all subsets containing nums[i] in the result!
            # continue recursing after undo
            part.pop()
            dfs(i + 1)
        
        dfs(0)
        return res


        