#number 1
vvod = float(input())
for i in range(1, 11):
    print((i / 10), "кг конфет =", round(vvod * (i / 10), 2), "руб")


#number 2
proiz = 1
vvod = int(input())
for i in range(1, vvod + 1):
    proiz = proiz * (1 + i / 10)
print(round(proiz, 3))


#number 3
vvod = int(input())
summ = 0
for i in range(1, 2 * vvod, 2):
    summ += i
    print(summ)


#number 4
a = float(input())
N = int(input())
summ = 0
for i in range(0, N + 1):
    summ += a**i
print(summ)

#number 5
a = float(input())
N = int(input())
summ = 1
min = 1
for i in range(0, N):
    min *= -a
    summ += min
print(summ)