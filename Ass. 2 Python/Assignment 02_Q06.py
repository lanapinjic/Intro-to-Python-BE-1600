import math

def inCircle():
    xpoint = int(input("Enter a x-value: "))
    ypoint = int(input("Enter a y-value :"))
    radius = int(input("Enter a radius: "))

    distance = math.sqrt((xpoint **2) + (ypoint **2))


    if (distance <= radius):
        print("Point(" , xpoint , "is in circle with radius", radius)

    if (distance >= radius):
        print("Point (", xpoint,",",ypoint,") is not in circle with radius", radius)

inCircle()
