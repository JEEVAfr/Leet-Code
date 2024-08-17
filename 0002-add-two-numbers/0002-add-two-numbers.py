# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create a list
        l1_value = []
        l2_value = []

        # append a l1 and l2 node in a l1 and l2 list
        current = l1
        while current is not None:
            l1_value.append(str(current.val))
            current = current.next

        current = l2
        while current is not None:
            l2_value.append(str(current.val))
            current = current.next

        # reverse a list
        l1_value = l1_value[::-1]
        l2_value = l2_value[::-1]

        # convert a str to int and join
        l1_number = int("".join(l1_value))
        l2_number = int("".join(l2_value))

        digit = str(l1_number + l2_number)[::-1]

        dummy = ListNode()
        current = dummy

        for i in digit:
            current.next = ListNode(int(i))
            current = current.next

        return dummy.next

        


