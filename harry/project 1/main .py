import random

'''
1 for snake
-1 for water
0 for gun
'''

youDict = {"s": 1, "w": -1, "g": 0}
reversDict = {1: "snake", -1: "water", 0: "gun"}

computer = random.choice([1, -1, 0])
youstr = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

if youstr not in youDict:
    print("invalied input! 's', 'w', ya 'g' likh.")
else: 
    you = youDict[youstr]

    print(f"Your choice: {reversDict[you]}")
    print(f"Computer's choice: {reversDict[computer]}")

    if computer == you:
        print("It's a draw!")
    elif computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You lose!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You lose!")
    else:
        print("Kuch mistake ho gaya dear 😂")
