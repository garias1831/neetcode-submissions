class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        if digits == '': return []

        
        lookup = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }

        res, part = [], []
        def dfs(i):
            if i >= len(digits):
                res.append("".join(part)) 
                return

            
            letters = lookup[digits[i]]
            for j in range(len(letters)):
                part.append(letters[j]) # explore
                dfs(i + 1)
                part.pop()
        
        dfs(0)
        return res





        