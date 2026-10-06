class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #Candidate triplet: All coords less than the target at that index
        #Ensures we either get the right coord, AND dont overwrite coords
        #Merging everything should give us target

        mergeres = [0, 0, 0]
        x, y, z = target
        print(x, y, z)

        for tpl in triplets:
            ai, bi, ci = mergeres
            #print(ai, bi, ci)
            
            #Check if candidate, if it is merge it
            if tpl[0] <= x and tpl[1] <= y and tpl[2] <= z:
                mergeres = [max(ai, tpl[0]), max(bi, tpl[1]), max(ci, tpl[2])]

           

        ai, bi, ci = mergeres
        print(f'mergeres:{mergeres}')
        if ai == x and bi == y and ci == z: #Foundit
            return True

        return False
            