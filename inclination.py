import math

x1=float(input("X1 - "))
x2=float(input("X2 - "))
y1=float(input("Y1 - "))
y2=float(input("Y2 - "))

m = (y2-y1)/(x2-x1)

result=(math.degrees(math.atan(m)))

print("Angle of Inclination - ",result,"Degrees")