class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == '': return []

        
        lookup = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res = []
        def dfs(i, s):
            if i >= len(digits):
                res.append(s) 
                return

            
            letters = lookup[digits[i]]
            for j in range(len(letters)):
                dfs(i + 1, s + letters[j])
        
        dfs(0, '')
        return res





        