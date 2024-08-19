# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast: # this work if there is a cycle
                break
            
        else:
            return None
        
        pointer = head

        while pointer != fast:
            pointer = pointer.next
            fast = fast.next

        
        return pointer


            