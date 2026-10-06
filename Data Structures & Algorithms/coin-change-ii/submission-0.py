class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Idea - brute force with cache
        # For each index i in coins, we want to cache the
        # remaining amount to match at that index

        # Cache of (i, leftover)
        # 0 <= i < coins
        # 1 <= leftover <= amt
        # Caching the index here, and the REMAINING
        # amount after picking some number of coins in the subsegment
        # coins[:i].
        # The value is the number of change at that idx.
        dp = {}
        #TODO: migh tnoe ned oaram
        def dfs(i, leftover):
            if (i, leftover) in dp:
                return dp[(i, leftover)]

            # Base cases
            if i >= len(coins):
                return 0

            # Calculate all possible leftover values -
            # This involves looping over all possible values
            # of times we could pick the coin at i
            # e.g if leftover = 7 and coins[i] = 2,
            # then we could pick coins[i] 0, 1, 2, or 3 times
            # giving leftover of 7, 5, 3, 1, 0
            times_picking_i = 0
            new_leftover = leftover
            num_combos = 0
            while (new_leftover) >= 0:
                # If we reach zero on this current case, c[i] & times
                # perfectly matches our current leftover, so we can't
                # do anything further here
                if (new_leftover == 0):
                    num_combos += 1
                    break
                
                # Else, sum up all the distinct combinations
                # From every other path
                num_combos += dfs(i + 1, new_leftover)
                
                times_picking_i += 1
                new_leftover = leftover - coins[i] * times_picking_i
            # Cache the result
            dp[(i, leftover)] = num_combos
            return num_combos
        return dfs(0, amount)
        

    


        