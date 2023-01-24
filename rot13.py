import string
# --------------------------------------
lowerAlpha = list(string.ascii_lowercase)*2
upperAlpha = list(string.ascii_uppercase)*2
userInpt = input("Enter your text : ")
for i in userInpt:
    if (i in lowerAlpha):
        print(lowerAlpha[lowerAlpha.index(i)+13],end='')
    elif (i in upperAlpha):
        print(upperAlpha[upperAlpha.index(i)+13],end='')
    else:
        print(i,end='')
        