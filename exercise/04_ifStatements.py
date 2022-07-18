price = 10 ** 6

has_good_credit = input('Has the buyer a good credit (Y/N)? ')

if 'Y' in has_good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price

print(f"Down payment required: ${down_payment}")