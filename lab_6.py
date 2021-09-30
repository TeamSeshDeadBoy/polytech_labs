#number 1
print("Введите А, B")
a, b = int(input()), int(input())
b, a = a, b
print("Переменные A, B поменяли свои значения: a - b, b - a:")
print(a, b)


#number 2
print("Введите А, B, C")
a, b, c = int(input()), int(input()), int(input())
b, c, a = a, b, c
print("Переменные A, B, C поменяли свои значения: a - b, b - c, c - a:")
print(a, b, c)


#number 3
print("Введите А, B, C")
a, b, c = int(input()), int(input()), int(input())
c, b, a = a, c, b
print("Переменные A, B, C поменяли свои значения: a - c, c - b, b - a:")
print(a, b, c)


#number 4
print("Введите переменную x = ")
x = int(input())
y = 3 * (x ** 6) - 6 * (x ** 2) - 7
print("В функции y = 3x^6 − 6x^2 − 7 при данном X ответ = ", y)


#number 5
print("Введите переменную x = ")
x = int(input())
y = 4 * ((x - 3) ** 6) - 7 * ((x - 3) ** 3) + 2
print("В функции y = 4(x−3)^6 − 7(x−3)^3 + 2 при данном X ответ = ", y)


#number 6
print("Введите переменную А = ")
A = int(input())
b = A * A
b = b * b
b = b * b
print("A^8, используя 1 вспомогательную переменную и три умножения = ")
print(b)


#number 7
print("Введите переменную А = ")
A = int(input())
b = A**2
c = A**3
b = b * b * b 
c = c * c * c 
A = c * b
print("A^15, используя 2 вспомогательные переменные и пять умножеений = ")
print(A)
