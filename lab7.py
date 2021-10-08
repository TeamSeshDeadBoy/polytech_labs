import numpy

#number 1 
pi = 3.14
print("Введите угол a в градусах, для перервода в радианы:")
a = float(input())
if a >= 0 and a <= 360:
    a = (a * pi) / 180  
    print("Значение a в радианах:", a)
else:
    print("Введено неверное значение. Конец программы.")
    

#number 2 
pi = 3.14
print("Введите угол a в радианах, для перервода в градусы:")
a = float(input())
if a >= 0 and a <= 2 * pi:
    a = (a * 180) / pi  
    print("Значение a в градусах:", a)
else:
    print("Введено неверное значение. Конец программы.")
    

#number 3 
print("Количество конфет, в кг:")
X = int(input())
print("Стоимость конфет, в руб:")
A = int(input())
print("Введите кол-во кг конфет для рассчета стоимости:")
Y = int(input())
print("1 кг конфет стоит:", A / X, "рублей.")
print(Y, "кг конфет стоит:", (A / X) * Y, "рублей.")


#number 4
print("Введите скорость 1 автомобиля (V1), км/ч:")
V1 = int(input())
print("Введите скорость 2 автомобиля (V2), км/ч:")
V2 = int(input())
print("Введите расстояние между автомобилями (S), км:")
S = int(input())
print("Введите время, для рассчета расстояния между ними (T), час:")
T = int(input())
V = V1 + V2
Sобщ = S + (V * T)
print("Расстояние между автомобилями через", T, "часа(ов) - ", Sобщ, "км.")


#number 5
print("Уравнение вида A * x + B = 0")
print("Введите ненулевой коэффициент A")
A = int(input())
print("Введите коэффициент B")
B = int(input())
if A != 0:
    x = B * (-1) / A
    print("X равен:", x)
else:
    print("А не может быть равен 0")


#number 6
print("Уравнение вида A1 * x + B1 * y = C1")
print("Введите ненулевой коэффициент A")
A1 = int(input())
print("Введите коэффициент B")
B1 = int(input())
print("Введите коэффициент C")
C1 = int(input())
print("Второе уравнение вида A2 * x + B2 * y = C2")
print("Введите ненулевой коэффициент A")
A2 = int(input())
print("Введите коэффициент B")
B2 = int(input())
print("Введите коэффициент C")
C2 = int(input())
if (A1 == 0 and A2 == 0) or (B1 == 0 and B2 == 0):
    print("Введены неверные исходные данные, одной из переменных нулевая. Конец программы.")
else:
    mas = numpy.array([[A1, B1],[A2, B2]])
    mas2 = numpy.array([[C1],[C2]])
    otvet = numpy.linalg.solve(mas, mas2)
    print("x =", otvet[0][0], "y = ", otvet[1][0])