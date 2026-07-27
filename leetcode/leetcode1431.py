class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = [False for _ in range(len(candies))]
        m = max(candies)

        for i in range(len(candies)):
            if candies[i] + extraCandies >= m:
                ans[i] = True
        
        return ans