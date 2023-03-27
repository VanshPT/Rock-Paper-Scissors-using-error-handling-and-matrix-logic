# Rock Paper Scissors game using matrix logic and full error handeling used.(One of the best versions of this game out there.)
import random
result=[("T","L","W"),("W","T","L"),("L","W","T")]
ch=1

while True:
    c=random.randrange(0,3,1)
    # print(c)
    try:
        p=int(input("Input from below!!!\n0:Rock\n1:Paper\n2:Scissors\n:"))
        if(result[p][c]=="T"):
            print("You Tied!!!\n")
        elif(result[p][c]=="W"):
             print("Congratulations!!!You Won\n")
        elif(result[p][c]=="L"):
            print("Sorry!!!You Lost\n")
    except:
        print("Wrong input!!!\n")
    ch=int(input("Enter: 0:exit,any number to replay:"))
    if(ch!=0):
        continue
    else:
        print("Thank you!!!Play again\n")
        break