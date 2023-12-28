a=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
   "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
   "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
   "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
   "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
shift=int(input("what is the shift number : "))
text=input("enter the word  : ")
opr=int(input("choose operation 1 = encryp , 2= dycryp : "))
def encrypt(normal_text,shift_no):
    res = ""
    for ltr in normal_text:
        posi=a.index(ltr)
        new_posi=posi + shift_no
        new_ltr = a[new_posi]
        res += new_ltr
    print(res)

def dycryp(normal_text,shift_no):
    res = ""
    for ltr in normal_text:
        posi=a.index(ltr)
        new_posi=posi - shift_no
        new_ltr = a[new_posi]
        res += new_ltr
    print(res)


if opr==1:
    encrypt(text,shift)
else:
    dycryp(text,shift)


