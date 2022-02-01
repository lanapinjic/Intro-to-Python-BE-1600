import math


def distance (x1,y1,x2,y2):
    return (math.sqrt(((x2-x1)**2) + ((y2-y1)**2)))
def radius (x1,y1,x2,y2):
    return distance(x1,y1,x2,y2)
def circumference(r):
    return (2 * 3.1416 * r)


xcorrdinate = float(input("Enter the x corordinate of the center of the circle: "))
ycorrdinate = float(input("Enter the y corordinates of the center of the circle: "))

xpoint = float(input("Enter the x corordinate of a point on the circle: "))
ypoint = float(input("Enter the y corordinates of a point on the circle: "))


print("Circle Radius = ",distance(xcorrdinate,ycorrdinate,xpoint,ypoint))
print("Circle Circumference = ",circumference(radius(xcorrdinate,ycorrdinate,xpoint,ypoint)))
