import random

rnd=random.randint(0,10)
print (rnd)

while True:
    usr_inp=int(input("enter a number between 0 and 10:")) 
    if usr_inp==rnd:
        print ("Right! That's all!")
        break
    elif rnd>usr_inp:
        print ("more")
    else rnd<usr_inp:
        print("less")
