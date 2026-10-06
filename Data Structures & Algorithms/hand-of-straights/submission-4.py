class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort() # Important


        groups = [] # Better if this is a like deque or something
        curr_group = 0

        prev = hand[0]
        for i in range(len(hand)):

            # Check if we've moved onto a new number - try appending to each one
            if prev != hand[i]:
                curr_group = 0

            # Appended to everything, create a new group            
            if curr_group == len(groups):
                if groupSize == 1:
                    prev = hand[i]
                    curr_group = 0
                    continue

                groups.append([hand[i]])
                curr_group += 1
                prev = hand[i]
                continue
            

            if groups[curr_group][-1] != hand[i] - 1:
                return False
            else:
                groups[curr_group].append(hand[i])

                if len(groups[curr_group]) == groupSize:
                    groups.pop(0) # TODO better if deque
                    curr_group = 0 
                else:
                    curr_group += 1
            
            prev = hand[i]




        return len(groups) == 0




        
        