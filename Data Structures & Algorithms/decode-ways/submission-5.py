class Solution:
    def numDecodings(self, s: str) -> int:

        # base cases
        if len(s) == 0: return 1
        if len(s) == 1: return 1 if s[0] != '0' else 0

        two_next_digits = [str(i) for i in range(0, 7, 1)]

        prev_prev = 0
        prev = 1

        curr = -1
        for i in range(len(s) - 1, -1 , -1):
            if s[i] == '0':
                prev_prev = prev
                prev = 0 # nothing can be formed at i
            elif s[i] == '1':
                curr = prev + prev_prev
                prev_prev = prev
                prev = curr
            elif s[i] == '2' and (i + 1) < len(s) and s[i + 1] in two_next_digits:
                curr = prev + prev_prev
                prev_prev = prev
                prev = curr
            else:
                prev_prev = prev
        
        return prev
        