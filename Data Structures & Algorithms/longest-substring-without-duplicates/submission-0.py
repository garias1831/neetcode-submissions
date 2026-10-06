class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Smart - the main idea here is that the window is ALLOWED
        # to dynamically grow and shrink .. it does NOT have to be fixed
        # Window will AT MOST contain the num of unique chars
        # Keep adding onto window right until you see dupe,
        # then keep popping from the left until that dupe is removed
        # sliding window does NOT have to be fixed

        seen = set()
        window = []
        best = 0

        for c in s:
            window.append(c)
            if c not in seen: 
                seen.add(c)
            else: # Dupe - remove from window
                while c in seen and len(window) > 0:
                    r = window.pop(0)
                    seen.remove(r)
                seen.add(c)

            if len(window) > best:
                best = len(window)
        
        return best


            


            
            



        