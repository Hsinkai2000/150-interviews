class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        """
        Calculates the maximum profit that can be obtained from buying and selling stocks.

        Args:
            prices (list[int]): A list of stock prices.

        Returns:
            int: The maximum profit that can be obtained.
        """
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
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
print(solution.maxProfit([7, 6, 4, 3, 1]))
print(solution.maxProfit([2, 4, 1]))
