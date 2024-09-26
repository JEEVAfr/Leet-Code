# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # find middle of the slow
        while fast and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        #reverse second half
        previous = None

        while slow is not None: # because current head is slow
        
            temp = slow.next
            slow.next = previous
            previous = slow
            slow = temp
        
        # check 
        left, right = head, previous # slow is going to be None and previous is behind of slow.

        while right is not None:
            if left.val == right.val:
                left = left.next
                right = right.next
            else:
                return False
        
        return True

        