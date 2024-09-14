# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:

        l1_value = []

        current = head

        while current is not None:
            l1_value.append(str(current.val))
            current = current.next
        
        l1_value = "".join(l1_value)
        print(l1_value)
        print(type(l1_value))

        decimal_value = int(l1_value, 2)

        return decimal_value


        