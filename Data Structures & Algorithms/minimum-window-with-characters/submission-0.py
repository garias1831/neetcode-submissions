class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s): return ""

        # Freq count on t
        need = {}
        for c in t:
            need[c] = 1 + need.get(c, 0)
        need_tot = sum(need.values()) # sum of all needed chars

        surplus = {} # Freq on surplusing chars

        # Answer
        lbest, rbest = 0, len(s) - 1
        bestlen = len(s) + 1

        l = 0
        for r in range(len(s)):
            c = s[r]
            if c in need:
                need[c] -= 1
                if need[c] >= 0:
                    need_tot -= 1
                else: # c goes into surplus
                    surplus[c] = 1 + surplus.get(c, 0)
            
            # Window invariants
            while l < r: 
                if s[l] not in need:
                    l += 1
                    continue

                if s[l] in surplus:
                    surplus[s[l]] -= 1
                    if surplus[s[l]] == 0:
                        surplus.pop(s[l])
                    l += 1
                    continue
                break

            # Update answer 
            if need_tot == 0 and (r - l + 1) < bestlen:
                bestlen = r - l + 1
                lbest, rbest = l, r
        
        res = ""
        if bestlen < len(s) + 1:
            res = s[lbest:rbest + 1]
        return res







        