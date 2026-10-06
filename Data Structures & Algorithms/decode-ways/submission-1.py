class Solution:
    def numDecodings(self, s: str) -> int:

        dp = {}

        def dfs(i):
            if i == len(s) - 1 and s[i] != '0':
                return 1
            if i == len(s):
                return 1
            elif s[i] == '0':
                return 0
            
            
            if i in dp:
                return dp[i]
           
            if s[i] == '1':
                dp[i] = dfs(i + 1) + dfs(i + 2)
            elif s[i] == '2':
                valid_next = [str(i) for i in range(0, 7, 1)]
                if (i + 1) < len(s) and s[i + 1] in valid_next:
                    dp[i] = dfs(i + 1) + dfs(i + 2)
                else:
                    dp[i] = dfs(i + 1)
            else:
                dp[i] = dfs(i + 1)
            
            return dp[i]
        
        return dfs(0)
            



        