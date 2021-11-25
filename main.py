#number 1
a = int(input())
b = int(input())
if ((a > 2) and ( b <= 3)):
    print("Высказывания верны")
else:
    print("Высказывания неверны")


#number 2
a = int(input())
b = int(input())
c = int(input())
if ((c > b) and ( b > a)):
    print("Высказывание верно")
else:
    print("Высказывание неверно")


#number 3
a = int(input())
if ((a % 2 == 0) and ( a / 100 < 1)):
    print("Высказывание верно")
else:
    print("Высказывание неверно")


#number 4
a = int(input())
one = a // 100
a = a - one * 100
two = a // 10
a = a - two * 10
three = a
if (((one > two) and (two > three)) or ((three > two) and (two > one))):
    print("Высказывание верно")
else:
    print("Высказывание неверно")


#number 5
a = int(input())
one = a // 1000
a = a - one * 1000
two = a // 100
a = a - two * 100
three = a // 10
a = a - three * 10
four = a
if (one * 10 + two == four * 10 + three):
    print("Высказывание верно")
else:
    print("Высказывание неверно")


#number 6
a = int(input())
b = int(input())
c = int(input())
if ((c^2 == a^2 + b^2) or (a^2 == c^2 + b^2) or (b^2 == c^2 + a^2)):
    print("Высказывание верно")
else:
    print("Высказывание неверно")


#number 7
a = int(input())
b = int(input())
c = int(input())
if (not(a < b + c) or not(b < a + c) or not(c < b + a)):
    print("Высказывание неверно")
else:
    print("Высказывание верно")