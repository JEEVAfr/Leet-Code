# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            previous, current = None, head

            while current is not None:
                temp = current.next
                current.next = previous
                previous = current
                current = temp
            
            return previous
        
        head = reverse(head)

        current = head
        cur_max = current.val

        while current.next is not None:
            if current.next.val < cur_max:
                current.next = current.next.next
            else:
                cur_max = current.next.val
                current = current.next
            
        return reverse(head)
