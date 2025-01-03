def maxProfit(prices):
    max_profit = 0
    min_price = prices[0]
    for i in range(1, len(prices)):
        if prices[i] < min_price:
            min_price = prices[i]
        else:
            max_profit = max(max_profit, prices[i] - min_price)
    return max_profit