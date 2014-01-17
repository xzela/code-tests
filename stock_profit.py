"""
A stock timeline is given which shows the history of a stock price
The price goes up and down throughout the day

We would like to figure out what would have been the maxiumn profit
if we have purchased and sold in the correct times

Example:
    timeline = 5,6,10,1,8
    max_profit = 7
    buying when the stock price was at 1 and then selling when it reached 8
    would result in 7 

Logic:
    set max_profit to 0
    set min_price to first entry in timeline

    loop through the timeline 
    if current price is less than min_price: 
        save current price as min_price
    if current price is greater than min_price
        if current price minu min_price is  greater than max_profit
            save product as max_profit
"""

timeline = [5,6,10,1,8,10,12,3,5,7]

max_profit = 0
max_price = 0
min_price = timeline[0];

print timeline

for num in timeline:
    if num < min_price:
        # print str(num) + " is min_price"
        min_price = num
    if num > min_price:
        # print str(num) + " is greater than min_price: " + str(min_price)
        if num - min_price > max_profit:
            max_price = num
            max_profit = num - min_price

print "Min Price: " + str(min_price)
print "Best Price: " + str(max_price)
print "Max Profit: " + str(max_profit)
