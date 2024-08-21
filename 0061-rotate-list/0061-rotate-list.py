# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head

        count = 0
        current = head

        while current is not None:
            count = count + 1
            current = current.next
        
        
        k = k % count

        if k == 0:
            return head
        
        current = head
        for i in range(count - k - 1):
            current = current.next
        newHead = current.next
        current.next = None
    
    
        original_tail = newHead
        while original_tail.next is not None:
            original_tail = original_tail.next
        original_tail.next = head
        


        return newHead


        

        


            
        