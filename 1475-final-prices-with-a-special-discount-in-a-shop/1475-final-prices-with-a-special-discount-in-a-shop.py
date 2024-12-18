class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
      def findDiscount(start, price):
        discount = 0
        for j in range(start, len(prices)):
          if prices[j] <= price:
            discount = prices[j]
            break
        return discount
      
      for i,p in enumerate(prices):
        prices[i] = p - findDiscount(i+1, p)
      return prices
          