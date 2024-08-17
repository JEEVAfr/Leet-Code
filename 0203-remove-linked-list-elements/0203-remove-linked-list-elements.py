# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current is not None :
            if current.val == val:
                previous.next = current.next
            else:
                previous = current
            
            current = current.next
        

        return dummy.next

        