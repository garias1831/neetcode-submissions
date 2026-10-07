class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        m = set()
        for x in nums:
            if x in m:
                return True
            m.add(x)
        return False        