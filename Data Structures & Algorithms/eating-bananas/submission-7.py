class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = 10

    

      

        while l <= r:

            middle = (l + r) // 2
            total = 0
            for p in piles:
                total += math.ceil(float(p)/middle)
            if total <= h:
                res = middle
                r = middle - 1
            else:
                l = middle + 1
        return res        

