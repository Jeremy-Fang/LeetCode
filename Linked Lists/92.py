# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        
        trav = head
        before = None
        
        while m > 1:
            before = trav
            trav = trav.next
            m -= 1
            n -= 1
        
        curr = prev = None
        after = None
        
        while n > 0:
            curr = trav
            if after == None:
                after = curr
            trav = trav.next
            curr.next = prev
            prev = curr
            n -= 1
        
        if before == None:
            head = prev
        else:
            before.next = curr
            
        after.next = trav
        
        return head
