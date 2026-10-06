class Solution:
    def search(self, nums: List[int], target: int) -> int:

        lo = 0
        hi = len(nums) - 1
        while lo < hi:
            mid = lo + (hi - lo) // 2
            print(mid)
            if nums[mid] >= target:
                hi = mid
            else:
                lo = mid + 1

        if nums[lo] == target:
            return lo
        return -1

        