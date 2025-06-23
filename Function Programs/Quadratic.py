import math

a=float(input("Enter the co-efficient a:"))
b=float(input("Enter the co-efficient a:"))
c=float(input("Enter the co-efficient a:"))

delta=b*b-4*a*c

if delta>0:
    root1=(-b+math.sqrt(delta))/(2*a)
    root2=(-b-math.sqrt(delta))/(2*a)
    print("Two distinct real roots:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif delta == 0:
    root = -b / (2 * a)
    print("One real root (repeated):", root)
else:
    realPart = -b / (2 * a)
    imagPart = math.sqrt(-delta) / (2 * a)
    print("Complex roots:")
    print("Root 1 =", realPart, "+", imagPart, "i")
    print("Root 2 =", realPart, "-", imagPart, "i")