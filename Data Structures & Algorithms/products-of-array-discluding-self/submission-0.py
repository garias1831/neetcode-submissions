class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Simple O(n) - take product of all numbers,
        # Then result[i] = prod / nums[i]

        # Idea - maintain a prefix and suffix array
        # Inclusive products up to i, i.e :
        # prefix[i] = nums[0] * nums[1] * ... * nums[i - 1]

        # Then exclusive products up to i also:
        # suffix[i] = nums[i + 1] * ... * nums[n - 1]

        prefix = [0] * len(nums)
        suffix = [0] * len(nums)
        prefix[0] = 1
        suffix[-1] = 1

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            suffix[i] = suffix[i + 1] * nums[i + 1]
        
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]
        
        return res

        