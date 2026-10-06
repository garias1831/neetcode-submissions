class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        s = deque()

        res = [0] * len(temperatures)
        for i in range(len(temperatures) - 1, -1, -1):
            while True:
                if len(s) == 0: break
                
                top, _ = s[-1]
                if top > temperatures[i]:
                    break
                s.pop()


            
            if len(s) == 0:
                res[i] = 0
            else:
                top, j = s[-1]
                res[i] = j - i

            s.append((temperatures[i], i))
            #print(i, s)

        return res
        
        