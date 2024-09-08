# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums = set(nums)
        count = 0

        curr = head

        while curr is not None:
            # Node is found in the hashset
            if curr.val in nums:
                # keep traversing next until it stops
                # increment connected component
                while curr.next and curr.next.val in nums:
                    curr = curr.next
                
                count += 1
            curr = curr.next
        
        return count



        