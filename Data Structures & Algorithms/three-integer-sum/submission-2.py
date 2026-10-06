class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:


        nums.sort()
        seen = set() # For dupe detection (will always have same order)
        res = []

        for i in range(0, len(nums) - 2, 1):

            target = -nums[i]
            l = i + 1
            r = len(nums) - 1
            while l < r:
                tot = nums[l] + nums[r]
                if tot > target:
                    r -= 1
                elif tot < target:
                    l += 1
                else:
                    # Tot == target
                    triple = (nums[i], nums[l], nums[r])
                    if triple not in seen:
                        seen.add(triple)
                        res.append(triple)
                    
                    # Neet to update both - if only update one,
                    # fixing 2 -> fixes the third, so only scrape dupes
                    l += 1
                    r -= 1

        return res
        