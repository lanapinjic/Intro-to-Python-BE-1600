#Future_Value, f=p*((1+i/100)**t), f=futurevalue, p=present value, i=monthly interest rate, t=#of months

def future_value (t,p,i):
    f = float(p * ((1 + i/100)**t))
    print("The information on your account is: ")
    print("Present Value: $", p)
    print("Interest Rate: %", i)
    print("After", t, "months, the value of your account will be $",f)

present_value = int(input("Please enter the present value of the account :"))
interest_rate = float(input("Please enter the interest rate of your account :"))
time = int(input("Please enter the number of months you would like to take into account:"))

future_value(time, present_value, interest_rate)
