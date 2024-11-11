price = round(float(input("Enter the price: ")), 2)
print price
paid = round(float(input("Enter the amount paid: ")), 2)
print paid
change = round(float(paid - price), 2)
print change
quarters = 0
dimes = 0
nickels = 0
pennies = 0
while change > 0.00:
    print change
    if change >= .25:
        change = change - .25
        quarters += 1
        continue
    elif change >= .1:
        change = change - .1
        dimes += 1
        continue
    elif change >= .05:
        change = change - .05
        nickels += 1
    elif change >= .01:
        change = change - .01
        pennies += 1
print "Quarters: " + str(quarters)
print "Dimes: " + str(dimes)
print "Nickels: " + str(nickels)
print "Pennies: " + str(pennies)