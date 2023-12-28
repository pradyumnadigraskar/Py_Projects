choice=int(input("enter the opr number \n 1 : Add \n 2 : sub \n 3 : mul \n 4 : div \n"))

def add(a,b):
     print(f"The addition of the number {a} and the number {b} is  = {a+b}")
    

def sub(a,b):
    print(f"The substraction of the number {a} and the number {b} is =  {a-b}")

def mul(a,b):
    print(f"The Multip of the number {a} and the number {b} is =  {a*b}")

def div(a,b):
    print(f"The div of the number {a} and the number {b} is =  {a/b}")


a=int(input("enter number to add : "))
b=int(input("enter number to add : "))


if choice==1:   
    add(a,b)
if choice==2:
    sub(a,b)
if choice==3:
    mul(a,b)
if choice==4:
    div(a,b)
