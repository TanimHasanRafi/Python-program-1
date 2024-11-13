from random import randint, random
for x in range( 1,6):
    guessnumber = int (input("enter the value:"))
    randomnumber = randint(1,5)
    if guessnumber == randomnumber:
        print("you have won")
    else:
        print("you are losing")
        print(randomnumber)