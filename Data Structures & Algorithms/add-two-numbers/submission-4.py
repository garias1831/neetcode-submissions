# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # Ez. but edge cases are annnoying to code:
    # Ec1: If one list is larger than the other, create dummy cells in the
    #      smaller one with value 0
    # Ec2: If both lists are the same side, but there is a carry e.g (8 + 7),
    #      then need to create the extra carry node outside of the main loop
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        p1 = l1
        p2 = l2
 
        res = ListNode() # Dummy initially
        cur = res

        carry = 0 
        while p1 or p2:
            v1 = p1.val if p1 else 0
            v2 = p2.val if p2 else 0
            
            dsum = v1 + v2 + carry

            if dsum >= 10:
                carry = 1
                cur.next = ListNode(dsum - 10, None)
            else:
                carry = 0
                cur.next = ListNode(dsum, None)

            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            cur = cur.next
        
        # Write the extra node if there is a carry
        if carry > 0:
            cur.next = ListNode(1, None)

         

        return res.next
            

        
        