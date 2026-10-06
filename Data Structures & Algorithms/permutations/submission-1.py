class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        

        def perm(left):
            if len(left) == 0:
                return []
            
            if len(left) == 1:
                return [[left.pop()]]

            res = []
            for k in left:
                nleft = left.copy()
                nleft.remove(k)

                partial_perms = perm(nleft)
                for pi in partial_perms:
                    pi.insert(0, k)
                    res.append(pi)
            return res


        return perm(set(nums))
