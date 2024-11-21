def total_calc(bill_amount, tip):
    total = bill_amount*(1+0.01*tip)
    total = round(total,2)
    print("The total bill is $",total)

total_calc(150,20)