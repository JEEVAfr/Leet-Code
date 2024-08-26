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

        result = []
        while right is not None:
            
            s = left.val + right.val

            if s:
                result.append(s)
            left = left.next
            right = right.next
        
        return max(result)
            

        