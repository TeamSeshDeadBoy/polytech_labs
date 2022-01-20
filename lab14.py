#number 1
a = int(input("Введите число А"))
b = int(input("Введите число B"))
for i in range(a, b + 1):
    print(str(i) * i)

#number 2
a = int(input("Введите число А"))
b = int(input("Введите число B"))
ostatok = a
while ostatok >= 0:
    ostatok -= b
print(ostatok + b)

#number 3
n = int(input("Введите число N"))
sum = 0
k = 0
while sum < n:
    k += 1
    sum += k
print(sum, k)

#number 4
s = 1000
k = 0
p = int(input("Введите P (0 < p < 25)"))
while s <= 1100:
    s += s * (p / 100)
    k += 1
print(k, s)

#number 5
a = int(input("Введите число А"))
b = int(input("Введите число B"))
while a != b:
    if a > b:
        a -= b
    else:
        b -= a
print(a)

#number 6
fib1 = 1
fib2 = 1
k = 2
f = 0
n = int(input("Введите N"))
while f < n:
    k += 1
    f = fib2 + fib1
    fib2 = fib1
    fib1 = f
print(k)
