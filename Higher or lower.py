import random

info={
    "Graphic Card" : 75000,
    "Moniter"      : 40000,
    "Consol"       : 50000,
    "Guitar"       : 8000,
    "Iphone"       : 100000,
    "speaker"      : 10000,
    "Microphone"   : 11000,
    "mouse"        : 3500,
    "TV"           : 80000,
    "WebCamera"    : 5000,
    "Samsung"      : 70000,
    "Smart Watch"  : 30000,
    "Mouse Pad"    : 4500
}

def rands():
    key, value = random.choice(list(info.items()))
    return key, value

end = True
key, value = rands()
while end:
 
    inp = input(f"Guess if next will have Greater value than {key} and {value} or less value\n")
    key2, value2 = rands()
    
    
    if inp == 'Higher' or inp == 'higher' or inp == 'High' or inp == 'high' or inp == 'Greater' or inp == 'greater' or inp == 'More' or inp == 'more':
        if value2 >= value:
            print("Congratulations! You guessed correctly.")
            print(f"The Value was {key2} and {value2} \n")
            key,value=key2,value2
        else:
            print("You Lost")
            print(f"The Value was {key2} and {value2} \n")
            end = False
            
    if inp == 'Lower' or inp == 'lower' or inp == 'Low' or inp == 'low' or inp == 'Less' or inp == 'less':
        if value2 <= value:
            print("Congratulations! You guessed correctly.")
            print(f"The Value was {key2} and {value2} \n")
            key,value=key2,value2
        else:
            print("You Lost")
            print(f"The Value was {key2} and {value2} \n")
            end = False