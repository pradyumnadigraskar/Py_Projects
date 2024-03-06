import random
cards={
    'A':'A',
    2:2,
    3:3,
    4:4,
    5:5,
    6:6,
    7:7,
    8:8,
    9:9,
    10:10,
    'J':10,
    'Q':10,
    'K':10
}

# USING IF ELSE LOGIC  #
# total=0

# draw=int(input("press 1 to draw a random card : "))
# if draw==1:
#     key, value = random.choice(list(cards.items()))
#     a=value
#     if a=='A':
#         value=11
#         print(f"The card is {key} and the value for that card is  {value}.")
#     print(f"The card is {key} and the value for that card is  {value}.")
# draw2=int(input("press 2 to draw a random card : "))
# if draw2==2:
#     key, value = random.choice(list(cards.items()))
#     b=value
#     if b=='A':
#         choice2=int(input("what value do you want 11 or 1 : "))
#         if choice2==1 or choice2==11:
#             print(f"The card is {key} and the value for that card is  {value}.")
#             b=choice2
#             print(f"The card is {key} and the value for that card is  {value}.")
#             total=a+b
#     print(f"The card is {key} and the value for that card is  {value}.")
#     total=a+b
#     print(f"your total is {total}")
#     if total==21:
#         print("Winner")
#     if total > 21:
#         print("you lost")
#     if total < 21:
#         draw3=int(input("press 3 to draw a random card : "))
#         if draw3==3:
#             key, value = random.choice(list(cards.items()))
#             print(f"The card is {key} and the value for that card is  {value}.")
#             c=value
#             total+=c
#             print(total)
#             if total==21:
#                 print("Winner")
#             if total > 21:
#                 print("you lost")
#         if total < 21:
#             draw4=int(input("press 4 to draw a random card : "))
#             if draw4==4:
#                 key, value = random.choice(list(cards.items()))
#                 print(f"The card is {key} and the value for that card is  {value}.")
#                 d=value
#                 total+=d
#                 print(total)
#                 if total > 21:
#                     print("you lost")
#                 if total==21:
#                     print("winner")

# Some times the condition or output never add up to 21 so we use looping logic 

#------------------------------------------------------------------------------------------------------------------------------

#USING LOOPS WITHOUT FUNCTIONS


# total=0


# while total<22:
#     inp=int(input("press 1 to draw card : "))
#     if inp==1:
#         key, value = random.choice(list(cards.items())) //takes random items (keys,value from dict)
#         if value=='A' and total==0:
#             value=11
#         if value=='A' and total!=0:
#             inp2=int(input("what value doo you need 1 or 11 : "))
#             value=inp2
            
#         print(f"The card is {key} and the value for that card is  {value}.")
#         total+=value

#         print(f"Your total is {total}")
#         if total==21:
#             print('winner')
#             break
#         if total>21:
#             print("loss")
#             break


#------------------------------------------------------------------------------------------------------------------------------


# USING FUNCTION



def blkJak(cards):

    total=0


    while total<22:
        inp=int(input("press 1 to draw card : "))
        if inp==1:
            key, value = random.choice(list(cards.items()))
            if value=='A' and total==0:
                value=11
            if value=='A' and total!=0:
                inp2=int(input("what value doo you need 1 or 11 : "))
                value=inp2
                
            print(f"The card is {key} and the value for that card is  {value}.")
            total+=value

            print(f"Your total is {total}")
            if total==21:
                print('winner')
                break
            if total>21:
                print("loss")
                break
            
            
        
            
blkJak(cards)
            















        

    
   
