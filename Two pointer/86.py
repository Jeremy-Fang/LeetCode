# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        curr = head
        g = g_curr = None
        l = l_curr = None
        
        while curr:
            if curr.val >= x:
                if g:
                    g_curr.next = ListNode(curr.val)
                    g_curr = g_curr.next
                else:
                    g = g_curr = ListNode(curr.val)
            else:
                if l:
                    l_curr.next = ListNode(curr.val)
                    l_curr = l_curr.next
                else:
                    l = l_curr = ListNode(curr.val)
            curr = curr.next
            
        if l_curr:
            l_curr.next = g
        else:
            l = g
        return l
