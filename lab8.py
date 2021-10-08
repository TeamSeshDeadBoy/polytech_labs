#number 1 
print("Введите размер файла в байтах:")
byte = int(input())
kbyte = byte // 1024
print("Вес файла в полных кб:", kbyte)


#number 2
print("Введите отрезок А:")
A = int(input())
print("Введите отрезок В:")
B = int(input())
kolvo = A // B
print("Полных отрезков В в А:", kolvo)


#number 3 
print("Введите отрезок А:")
A = int(input())
print("Введите отрезок В:")
B = int(input())
kolvo = A % B
print("Незанятая часть отрезка А:", kolvo)


#number 4
print("Введите двузначное число:")
A = int(input())
B = str(A // 10 + A % 10 * 10)
print("Перевернутое число В:", B)


#number 5
print("Введите трехзначное число:")
A = int(input())
B = str(A // 100 + A % 100 * 10)
print("Перевернутое число В:", B)
