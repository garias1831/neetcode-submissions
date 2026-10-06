class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        # left[c] = how many more copies of c we need
        left = {}
        for c in s1:
            left[c] = left.get(c, 0) + 1

        # Number of individual character requirements satisfied
        total = 0

        l, r = 0, 0
        while r < len(s2):

            # Add s2[r]
            if s2[r] in left:
                left[s2[r]] -= 1

                # We satisfied a required copy iff we went
                # from needing >= 1 copies to needing >= 0.
                if left[s2[r]] >= 0:
                    total += 1

            # Window too large: remove s2[l]
            if r - l + 1 > len(s1):
                if s2[l] in left:
                    # If we're removing a character that was
                    # actually satisfying a requirement, total--
                    if left[s2[l]] >= 0:
                        total -= 1

                    left[s2[l]] += 1

                l += 1

            if total == len(s1):
                return True

            r += 1

        return False