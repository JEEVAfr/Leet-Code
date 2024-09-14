# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # convert linked list to list
        res = []
        current = head

        while current is not None:
            res.append(current.val)
            current = current.next

        # using merge sort   
        def mergesort(res):

            if len(res) <= 1:
                return res
            
            middle = len(res) // 2
            left_half = res[:middle]
            right_half = res[middle:]

            left_half = mergesort(left_half)
            right_half = mergesort(right_half)

            left = 0
            right = 0
            check_pointer = 0

            while left < len(left_half) and right < len(right_half):

                if left_half[left] < right_half[right]:
                    res[check_pointer] = left_half[left]
                    left += 1
                    check_pointer += 1
                else:
                    res[check_pointer] = right_half[right]
                    right += 1
                    check_pointer += 1
            
            while left < len(left_half):
                res[check_pointer] = left_half[left]
                left += 1
                check_pointer += 1
            
            while right < len(right_half):
                res[check_pointer] = right_half[right]
                right += 1
                check_pointer += 1
            
            return res
        
        # convert list to linked list   
        dummy = ListNode()
        current = dummy

        for i in mergesort(res): # direct use the function
            current.next = ListNode(i)
            current = current.next
    
        return dummy.next

    
            



        