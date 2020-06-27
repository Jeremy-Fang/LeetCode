# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        trav = head
        res = None
        prev = first = second = None
        
        if trav == None:
            return None
        
        while trav:
            if trav and trav.next:
                # there are two elements and we swap
                first = trav
                second = trav.next
                #increment by 2
                trav = trav.next.next
                first.next = trav
                second.next = first
                if prev == None:
                    res = second
                else:
                    prev.next = second
                
                prev = first
            else:
                # there's one element left so add to the end
                if prev == None:
                    res = trav
                else:
                    prev.next = trav
                trav = trav.next
        
        return res
            
