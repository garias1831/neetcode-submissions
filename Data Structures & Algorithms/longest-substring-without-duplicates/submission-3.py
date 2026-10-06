class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        max_length, length = 0, 0

        chars = set() # O(1) space
        while r < len(s):

            while l < r:
                if s[r] not in chars:
                    break
                
                chars.remove(s[l]) # Invariant: all chars in s[l : r + 1] unique
                l += 1
                length -= 1
                    
            
            chars.add(s[r])
            length += 1
            r += 1
            max_length = max(max_length, length)
                
        return max_length
