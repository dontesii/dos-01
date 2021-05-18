import math
x1=int(input("Введите x1 : "))
y1=int(input("Введите y1 : "))
x2=int(input("Введите x2 : "))
y2=int(input("Введите y2 : "))

from math import sqrt
dist = sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))



print("Расстояние между точками:", dist )
