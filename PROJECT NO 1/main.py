'''
1 is for snake
-1 for water 
0 for gun

'''
import random

computer = random.choice([1, 0, -1])
youstr = input("enter your choice: ").lower()
 
youDict ={
    "s": 1,
    "w": -1,
    "g": 0
}
reverseDict ={
    1: "snake",
    -1: "water",
    0: "gun"
}
you = youDict[youstr]

# by we have teo numbers variavle : you and compiter

print(f"you chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")


if (computer== you):
    print("draw")
else:   
    if(computer == -1 and you == 1):
        print("you win")

    elif(computer == -1 and you == 0):
        print("you lose")

    elif(computer == 1 and you == -1):
        print("you lose")

    elif(computer == 1 and you == 0):
        print("you WIn")

    elif(computer == 0 and you == -1):
        print("you win")

    elif(computer == 0 and you == 1):
        print("you lose")

    else:
        print("went wrong")



# if((computer-you)== -1 or (computer-you) == 2):
#     print("you lose")
# else:
#     print("you win")   
# its just a your logic but not a readable its logic by value of computer - value of you 
#   if the subtraction of both is (-1,2 ) then you lose the game 