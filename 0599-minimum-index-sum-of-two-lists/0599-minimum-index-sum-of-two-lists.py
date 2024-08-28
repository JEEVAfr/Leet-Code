class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        
        a = {} # dict
                                             # name   : index
        for index, name in enumerate(list1): # shogum : 0 
            a[name] = index

        min_sum = 100000 
        result = []

        for i, n in enumerate(list2):
            if n in a:
                total = a[n] + i # Calculate index sum for the common string
                if total < min_sum:
                    min_sum = total
                    result = [n] # Reset result with the new minimum index sum string
                elif total == min_sum:
                    result.append(n) # if index sum matches the current minimum
        
        return result

        