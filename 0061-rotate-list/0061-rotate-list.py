# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: #check the head 
            return head

        length = 1
        current = head

        while current.next is not None:
            current = current.next
            length += 1

        k = k % length
           
        if k == 0:
            return head
        
    
        cur = head
        for i in range(length - k - 1):
            cur = cur.next
        newHead = cur.next
        cur.next = None
        current.next = head

        return newHead