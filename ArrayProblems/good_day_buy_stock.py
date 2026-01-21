def maxProfit(prices):
    minimum_price = prices[0]
    max_profit = 0
    for price in prices[1:]:
        if price < minimum_price:
            minimum_price = price
        else:
            max_profit = max(max_profit, price - minimum_price)
    return max_profit