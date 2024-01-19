import random as r
your_score=0
oponent_score=0
times=int(input("how many times you want to play this game "))
l=["snake","water","gun"]
for i in range(times):
    your_choice=input("enter your choice")
    oponent_choice=r.choice(l)
    print(f"oponent choice {oponent_choice}")
    if(((your_choice=="gun")and(oponent_choice=="snake"))or((your_choice=="water")and(oponent_choice=="gun")or((your_choice=="snake")and(oponent_choice=="water")))):
        your_score+=1
        print("you win")
    elif(your_choice==oponent_choice):
         print("tie")
    else:
        oponent_score+=1
        print("oponent win")
       

print(your_score)
print(oponent_score)
    
if(your_score>oponent_score):
        print("you win")
elif(your_score==oponent_score):
        print("tie")
else:
        print("oponent win")

