# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_value = []
        l2_value = []

        current = l1
        while current is not None:
            l1_value.append(str(current.val))
            current = current.next
        
        current = l2
        while current is not None:
            l2_value.append(str(current.val))
            current = current.next


        # convert a str to int and join
        l1_number = int("".join(l1_value))
        l2_number = int("".join(l2_value))

        digit = str(l1_number + l2_number)

        dummy = ListNode()
        current = dummy

        for i in digit:
            current.next = ListNode(int(i))
            current = current.next

        return dummy.next

        


