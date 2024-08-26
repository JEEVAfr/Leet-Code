# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        fast = head
        slow = head

        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        previous = None

        while slow is not None:

            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp
        
        left , right = head, previous

        max_sum = 0
        while right is not None:
            
            s = left.val + right.val
            max_sum = max(max_sum, s)

            
            left = left.next
            right = right.next
        
        return max_sum
            

        