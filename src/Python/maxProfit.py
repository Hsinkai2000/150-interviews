class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        
        # Solution is Too slow

        # maxProfit=0
        # newPrices = prices.copy()
        # for i in range(len(prices)):
        #     if max(newPrices) > prices[i] and maxProfit < max(newPrices)-prices[i]:
        #         maxProfit = max(newPrices)-prices[i]
        #     newPrices.remove(prices[i])
        # return maxProfit

        maxProfit = 0
        minPrice = prices[0]

        for price in prices:
            currentProfit = price - minPrice
            if currentProfit > maxProfit:
                maxProfit = currentProfit
            if price < minPrice:
                minPrice = price
        
        return maxProfit

    
solution = Solution()
print(solution.maxProfit([7,1,5,3,6,4]))
print(solution.maxProfit([7,6,4,3,1]))
print(solution.maxProfit([2,4,1]))
