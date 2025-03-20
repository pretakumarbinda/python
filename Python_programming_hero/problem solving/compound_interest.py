# take the input of money, interest and time and calculate the compound interest

def compound_interest(principle, rate, time):
    interest = principle * ((1+ rate/100) ** time)
    return interest
printciple = int(input("money you borrowed: "))
interest_rate = float(input("interest rate: "))
time = float(input("overall duration: "))
total_due = compound_interest(printciple, interest_rate, time)
print("interest amount is: ", total_due)