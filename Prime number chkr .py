a=int(input("Enter the number : "))

def p_n_c(a):
    is_prime = True
    for i in range(2,a):
        if a%i == 0:
            is_prime = False
    if is_prime:
        print(f"the given number {a} is prime")
    else:
        print(f"the given number {a} is Non_Prime")
p_n_c(a)