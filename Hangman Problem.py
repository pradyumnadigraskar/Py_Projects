import random

disp=[]
list=["mouse","keybord","microphone","webcam","display","headphone","cabinet","speaker","motherbord","graphicscard"]
l2=['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
'''
 ]

choosen_word = random.choice(list)
print(choosen_word)

for letter in choosen_word:
    disp += "-"
print(disp)
eog=False
a=6
while "-" in disp and a!=0:
    win=False
    guess=input("guess a letter : ").lower()
    if a!=0:
        for posi in range(len(choosen_word)):
            letter = choosen_word[posi] 
            if letter == guess:
                disp[posi]= letter
                win=True
    if not win:
        a-=1
        print(a)         
        print(l2[5 - a])
        if a==0:
            print("LOSER")
            break
                         
    print(disp)
print("Winner")
    


    


