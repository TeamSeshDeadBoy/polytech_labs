#number 1
edinici = ["первое", "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое"]
desyatki = ["десятое", "одиннадцатое", "двенадцатое", "тринадцатое", "четврнадцатое", " пятнадцатое", "шестнадцатое", "семнадцатое", "восемнадцатое", "девятнадцатое", "двадцатое"]
bolshe = ["двадцать", "тридцать"]
mesyac = ["января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"]
vvod1 = int(input())
vvod2 = int(input())

if vvod1 < 10:
    print(edinici[vvod1 - 1], mesyac[vvod2 - 1])
elif (vvod1 >= 10) and (vvod1 <= 20):
    print(desyatki[vvod1 - 10], mesyac[vvod2 - 1])
else:
    print(bolshe[vvod1 // 10 - 2], edinici[vvod1 % 10 - 1], mesyac[vvod2 - 1])


#number 2
napr = 0
stor = ["С", "В", "Ю", "З", "С", "З"]
vvod1 = input()
if vvod1 == "С":
    napr = 0
elif vvod1 == "В":
    napr = 1
elif vvod1 == "Ю":
    napr = 2
else:
    napr = 3
vvod2 = int(input())
if vvod2 == 0:
    print(vvod1)
elif vvod2 == 1:
    print(stor[napr - 1])
elif vvod2 == -1:
    print(stor[napr + 1])


#number 3
variants = ["учебное задание", "учебных задания", "учебных заданий"]
odin = ["одно", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
dva = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четырнадцать", " пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать"]
tri = ["десять", "двадцать", "тридцать", "сорок"]
vvod = int(input())
if vvod == 1:
    print(odin[vvod - 1], variants[0])
elif vvod > 1 and vvod < 5:
    print(odin[vvod - 1], variants[1])
elif vvod >= 5 and vvod < 10:
    print(odin[vvod - 1], variants[2])
elif vvod >= 10 and vvod <= 20:
    print(dva[vvod - 10], variants[2])
elif vvod == 20 or vvod == 30 or vvod == 40:
    print(tri[vvod // 10 - 1], variants[2])
elif vvod == 21 or vvod == 31:
    print(tri[vvod // 10 - 1], odin[0], variants[0])
elif vvod > 21 and (vvod % 10 == 2 or vvod % 10 == 3 or vvod % 10 == 4):
    print(tri[vvod // 10 - 1], odin[vvod % 10 - 1], variants[1])
else:
    print(tri[vvod // 10 - 1], odin[vvod % 10 - 1], variants[2])


#number 4
edinici = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"]
desyatki = ["десять", "одиннадцать", "двенадцать", "тринадцать", "четврнадцать", " пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать", "двадцать"]
bolshe = ["двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"]
eshe_bolshe = ["сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"]
vvod = int(input())
if vvod % 100 == 0:
    print(eshe_bolshe[vvod // 100 - 1])
elif vvod % 100 < 10:
    print(eshe_bolshe[vvod // 100 - 1], edinici[vvod % 10 - 1])
elif vvod % 100 >= 10 and vvod % 100 < 20:
    print(eshe_bolshe[vvod // 100 - 1], desyatki[vvod % 10])
elif (vvod % 10) == 0 and (vvod % 100) > 19:
    print(eshe_bolshe[vvod // 100 - 1], bolshe[(vvod // 10) % 10 - 2])
else:
    print(eshe_bolshe[vvod // 100 - 1], bolshe[(vvod // 10) % 10 - 2], edinici[vvod % 10 - 1])


#number 5
vvod = int(input())
nachalo = 1984
odin = ["зеленой", "красной", "желтой", "белой", "черной"]
odin_tig = ["зеленого", "красного", "желтого", "белого", "черного"]
dva = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]
raznica = vvod - nachalo
if ((raznica % 60) % 12) == 2 or ((raznica % 60) % 12) == 3 or ((raznica % 60) % 12) == 4:
    print("Год", odin_tig[((raznica % 60) // 12)], dva[((raznica % 60) % 12)])
else:
    print("Год", odin[((raznica % 60) // 12)], dva[((raznica % 60) % 12)])
