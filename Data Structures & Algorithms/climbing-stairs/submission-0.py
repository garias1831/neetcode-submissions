class Solution:
    def climbStairs(self, n: int) -> int:
        
        #Wrapper with #stairs, and a hashtable containing
        #What we've already seen
        def stair_count(n, stairs_seen):
            if n < 1:
                return 0
            if n == 1:
                return 1
            if n == 2: #Not sure if i need this
                return 2

            if n not in stairs_seen:
                stairs_seen.add(n)
            
            up1 = stair_count(n - 1, stairs_seen)
            up2 = stair_count(n - 2, stairs_seen)
            return up1 + up2


        return stair_count(n, set())

        