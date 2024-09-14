# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = []

        current = head

        while current is not None:
            res.append(current.val)
            current = current.next
        
        for i in range(1, len(res)):
            cur = res[i]
            j = i - 1
            while j >= 0 and cur < res[j]:
                res[j + 1] = res[j]
                j -= 1
            res[j + 1] = cur
        

        dummy = ListNode()
        current = dummy

        for i in res:
            current.next = ListNode(i)
            current = current.next
        
        return dummy.next
