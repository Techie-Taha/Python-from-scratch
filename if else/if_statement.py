#price of a house is 1000000
price = 1000000
#if buyer has good credit, need to put down 10% otherwise 20%, print the down payment
has_good_credit = True
if has_good_credit:
    down_payment = 0.1 * int(price)
else:
    down_payment = 0.2 * int(price)
#formatted string
print(f' ${down_payment} is the down payment')
#print(down_payment)