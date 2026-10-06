class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        lis = [1] * len(nums)

        for i in range(len(nums), -1, -1):

            # If the num we want to add is less than the start index of the desired,
            # Then we can increase the current lis. If not, the max at that index is just
            # a singleton
            for j in range(i + 1, len(lis)):
                if nums[i] < nums[j]:
                    lis[i] = max(lis[i], 1 + lis[j])


        return max(lis)
            
        