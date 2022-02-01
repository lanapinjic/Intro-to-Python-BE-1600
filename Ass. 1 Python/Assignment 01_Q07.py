
import math

def function():
    
    Gallon = math.ceil(float(sq/115))
    laborHours = math.ceil(float(Gallon *8))
    paintCharge = float(Gallon*price)
    laborCharge = (laborHours*20)
    totalCost = float(paintCharge+ laborCharge)
    print("Gallons of Paint: ", Gallon)
    print("Hours of labor: ", laborHours)
    print("Paint Charges: $", paintCharge)
    print("Labor Charges: $", laborCharge)
    print("Total Hours: $ ", totalCost)


sq = float(input("Enter wall space in square feet: "))
price = float(input("Enter paint price per gallon: "))

function()
