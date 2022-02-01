def total_sales (m):
    s = float(int(m*0.04))
    c = float(int(m*0.02))
    t = float(int(s+c))
    print("Monthly sales: $", m)
    print("State tax: $", s)
    print("County tax: $", c)
    print("Total tax: $",t)


monthly_sales = float(input("Enter the total sales for the month: "))
total_sales(monthly_sales)
