from math import sqrt 


#number 1
print("Введите координаты двух точек для рассчета расстояния между ними в формате (x, y)") 
x1, y1 = int(input()), int(input()) 
x2, y2 = int(input()), int(input()) 
ras = sqrt((x2 - x1)**2 + (y2 - y1) ** 2) 
print("Расстояние от точки до точки = ", ras)


#number 2
print("Введите три точки a, b, c для рассчета расстояний между ними :")
a, b, c = int(input()), int(input()), int(input())
rasac = abs(c - a)
rasbc = abs(c - b)
print("Расстояние от точки до точки A до C = ", rasac) 
print("Расстояние от точки до точки B до C = ", rasbc) 
print("Сумма расстояний = ", rasac + rasbc)


#number 3
print("Введите три точки a, b, c для рассчета расстояний между ними :")
a, b, c = int(input()), int(input()), int(input())
if (c < b) and (c > a):
    rasac = abs(c - a)
    rasbc = abs(c - b)
    print("Расстояние от точки до точки A до C = ", rasac) 
    print("Расстояние от точки до точки B до C = ", rasbc) 
    print("Произведение расстояний = ", rasac * rasbc)
else:
    print("Точка C не соответствует условию.")


#number 4
print("Введите координаты противоположных вершин прямоугольника (x, y):")
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
dlin = abs(x2 - x1)
shir = abs(y2 - y1)
print("Периметр прямоугольника P = ", 2 * (dlin + shir)) 
print("Площадь прямоугольника S = ", dlin * shir) 


#number 5
print("Введите координаты трех вершин треугольника (x, y):")
x1, y1 = int(input()), int(input())
x2, y2 = int(input()), int(input())
x3, y3 = int(input()), int(input())
plosh = 0.5 * abs((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1))
print("Площадь треугольника S = ", plosh) 