class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # Map value to index of first consumed
        need = {}

        for i, x in enumerate(nums):
            if x in need:
                return [need[x], i]
            
            leftover = target - x
            need[leftover] = i
        
        return []

            
                



        