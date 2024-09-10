# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = head
        current = head.next

        while current is not None:

            gcd = math.gcd(prev.val, current.val)
            g = ListNode(gcd)
            prev.next = g
            g.next = current
            prev = current
            current = current.next
            
        
        return head
        