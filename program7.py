number1 = 20
number2 = 90
number3 = 50

if number1>number2:
    if number1> number3:
        print("number3",+number3)
    else:
        print(number3)

if number2>number1:
    if number2> number3:
        print("number2 :",+number2)
    else:
        print(number3)

number4=00
number5=30
number6=40

if number4> number5 and number4> number6:
    print(number4)

elif number5> number4 and number5> number6:
    print(number5)
else:
    print(number6)

marks=55
if 80<=marks<=100:
    print("A+")

elif 70 <= marks <= 80:
        print("A")
elif 60<=marks<=70:
    print("A-")
else:
    print("Fail")