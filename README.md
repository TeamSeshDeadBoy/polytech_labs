# polytech_labs
laboratorniye dlya polytecha =)
Lebedev Stepan Vasil'evich


lab5
# number 1
from math import sqrt
print("Введите координаты двух точек для рассчета расстояния между ними в формате (x, y)")
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
ras = sqrt((x2 - x1)**2 + (y2 - y1) ** 2)
print("Расстояние от точки до точки = ", ras)

# number 2
print("Введите координаты точек a, b, c для рассчета расстояний между ними в формате (x, y)")
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())
rasac = sqrt((x3 - x1)**2 + (y3 - y1) ** 2)
rasbc = sqrt((x3 - x2)**2 + (y3 - y2) ** 2)
print("Расстояние от точки до точки A до C = ", rasac)
print("Расстояние от точки до точки B до C = ", rasbc)
print("Сумма расстояний = ", rasac + rasbc)

# number 3 
