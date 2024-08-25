# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        previous = dummy
        current = head

        while current is not None and current.next is not None:
            # save pointers

            next_pair = current.next.next
            second = current.next

            # reverse

            second.next = current
            current.next = next_pair
            previous.next = second


            previous = current
            current = next_pair

        
        return dummy.next


        