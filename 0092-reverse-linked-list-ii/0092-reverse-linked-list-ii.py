# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        for i in range(left - 1):
            previous = current
            current = current.next
        
        lp = previous
        prev = None
        
        for i in range(right - left + 1):
            
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        
        lp.next.next = current
        lp.next = prev
        

        return dummy.next
            