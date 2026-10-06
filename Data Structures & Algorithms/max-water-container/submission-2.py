class Solution:
    def maxArea(self, heights: List[int]) -> int:

        
        area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = max(area, min(heights[l], heights[r]) * (r - l))

            # if heights[l + 1] > heights[l]:
            #     l += 1
            # elif heights[r - 1] > heights[r]:
            #     r -= 1
            #else: # TODO -- too simple transition
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
                

        return area

        