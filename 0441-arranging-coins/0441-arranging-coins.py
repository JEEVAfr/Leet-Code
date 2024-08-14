class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 1
        right = n
        res = 0

        while left <= right: 
            mid = (left + right) // 2 # guass formula (n / 2) * (n + 1) 
                                      # n represent total number
            coins = (mid / 2) * (mid + 1)

            if coins > n:
                right = mid - 1
            else:
                left = mid + 1

                res = mid  # `mid` will always be the largest valid `mid` when the loop exits
                            # max(mid, res)
            
        return res

        