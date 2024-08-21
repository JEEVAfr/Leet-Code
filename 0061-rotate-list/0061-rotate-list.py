# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None: #check the head 
            return head

        length = 1 # calculate the length of the list
        tail = head

        while tail.next is not None:
            tail = tail.next
            length += 1
        
        
        k = k % length # bcoz if k is greater 

        if k == 0:   # k is 0 there is not rotation
            return head
        
        current = head # traverse 
        for i in range(length - k - 1): # 5 - 2 = 3 first node start with 1
            current = current.next     # 3 - 1 = 2
        newHead = current.next
        current.next = None
        tail.next = head

        return newHead


        

        


            
        