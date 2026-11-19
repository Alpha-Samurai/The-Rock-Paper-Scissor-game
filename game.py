'''

1 for rock
2 for paper
3 for scissor
'''
import random

while True :

    computer=random.choice([1,2,3])

    p1=input("Enter your choice to begin \n R for rock \n P for paper \n S for scissor : ")

    playerDict={"R":1 , "P":2 , "S":3}
    player=playerDict[p1]
    reverseDict={1:"Rock", 2:"Paper", 3:"Scissor"}

    if p1 not in playerDict:
        print("Invalid Input")
        continue

    print(f"\n You chose {reverseDict[player]} \n Computer chose {reverseDict[computer]}")

    if (computer==3 and player==3):
        print("\nThat's a Draw")

    elif(computer==3 and player==1):
        print("\nYou Won !! ")

    elif(computer==3 and player==2):
        print("\n Opps You Lost, Better Luck Next Time ")

    elif(computer==1 and player==1):
        print("\nThat's a Draw")

    elif(computer==1 and player==2):
        print("\nYou won !!")

    elif(computer==1 and player==3):
        print("\n Opps You Lost, Better Luck Next Time ")

    elif(computer==2 and player==1):
        print("\n Opps You Lost, Better Luck Next Time ")

    elif(computer==2 and player==2):
        print("\nThat's a Draw")

    elif(computer==2 and player==3):
        print("\nYou Won !!")

    else:
        print("\nOopss Something went Wrong")

    a=input("\n If you want to play again type 'Yes' \n If you want to quit type 'No' : ")

    if(a=="Yes"):
        continue 
    
    elif(a=="No" or a=="no" or a=="NO"):
        print("Thanks for playing !!")
        break

# GG