import random 



inp1=int(input("Enter Difficulty \n 1 : Easy \n 2 : Medium \n 3 : Hard \n "))

if inp1==1:
    num=random.randint(0,50)
    print("You Have 15 chance")
    a=15
    while a > -1:
        inp2=int(input("Guess The Number between 0 to 50 \n "))
        if inp2==num:
            print("you won")
            break
        if inp2>num:
            print("The number is smaller than gussed number ")
            a-=1
            print(f"Now you have {a} chances left")
        if inp2<num:
                print("The number is bigger  than gussed number ")
                a-=1
                print(f"Now you have {a} chances left")
        if a==0:
             print(f"You lost the Number was {num}")


if inp1==2:
    num=random.randint(0,100)
    print("You Have 10 chance")
    a=10
    while a > -1:
        inp2=int(input("Guess The Number between 0 to 100 \n "))
        if inp2==num:
            print("you won")
            break
        if inp2>num:
            print("The number is smaller than gussed number ")
            a-=1
            print(f"Now you have {a} chances left")
        if inp2<num:
                print("The number is bigger  than gussed number ")
                a-=1
                print(f"Now you have {a} chances left")
        if a==0:
             print(f"You lost the Number was {num}")

if inp1==3:
    num=random.randint(0,1000)
    print("You Have 5 chance")
    a=5
    while a > -1:
        inp2=int(input("Guess The Number between 0 to 1000 \n "))
        if inp2==num:
            print("you won")
            break
        if inp2>num:
            print("The number is smaller than gussed number ")
            a-=1
            print(f"Now you have {a} chances left")
        if inp2<num:
                print("The number is bigger  than gussed number ")
                a-=1
                print(f"Now you have {a} chances left")
        if a==0:
             print(f"You lost the Number was {num}")
             break


            


