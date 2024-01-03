import math
x = float(input("Insert x: "))
if x < 1:
    e = math.e ** math.sqrt(x)
    q = 1 - x
    y = math.sqrt(q)
    z = e / y
    print("z =", z)
else:
    print("Insert x < 1")
from mod import calculate_product