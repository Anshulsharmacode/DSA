prices = [7, 1, 5, 3, 6, 4]

profit = float('-inf')
min_price = float('inf')

for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)