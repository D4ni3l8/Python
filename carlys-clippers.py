hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Loop through the prices list and add each price to the variable total_price.
total_price = 0
for price in prices:
  total_price += price

# average price of haircut
average_price = total_price / len(prices)
print("Average haircut price: " + str(average_price))

# removing $5 for each haircut
new_prices = [price - 5 for price in prices]
print(new_prices)

# calculating total revenue
total_revenue = 0
for i in range(0, len(hairstyles)):
  total_revenue += prices[i] + last_week[i]
print("Total revenue: " + str(total_revenue))

average_daily_revenue = total_revenue / 7 # daily revenue
print(average_daily_revenue)

# displaying haircuts under $30
cuts_under_30 = [hairstyles[i] for i in range(0, len(new_prices)) if new_prices[i] < 30]
print(cuts_under_30)
