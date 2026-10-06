class Solution:
    def trap(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        moved_left = False

        total = 0
        level = 0
        while l < r:
            # Subtract off bar heights previously submerged
            if moved_left:
                total -= min(height[l], level)
            else:
                total -= min(height[r], level)
            
            newlevel = min(height[l], height[r])
            if newlevel > level:
                # Water level increased: add to the total
                h = (newlevel - level)
                w = r - l - 1
                total += h * w
                # Update new bigger level
                level = newlevel

            # Move pointer
            if height[l] <= height[r]:
                l += 1
                moved_left = True
            else:
                r -= 1
                moved_left = False     

        return total

        