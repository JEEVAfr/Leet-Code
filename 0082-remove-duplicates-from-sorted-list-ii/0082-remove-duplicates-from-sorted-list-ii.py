# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current is not None:
            if current.next is not None and current.val == current.next.val:
                while current.next is not None and current.val == current.next.val:
                    current = current.next
                previous.next = current.next
            else:
            
                previous = current
        
            current = current.next

        return dummy.next
        