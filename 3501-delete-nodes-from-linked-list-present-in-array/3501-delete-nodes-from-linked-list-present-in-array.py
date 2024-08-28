# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

        a = set(nums)

        dummy = ListNode(0, head)

        current = dummy
        
        while current is not None and current.next is not None:
            if current.next.val in a:  
                current.next = current.next.next  
            else:
                current = current.next
        
        return dummy.next
        