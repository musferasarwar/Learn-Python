import random

def game():
    print("you are playing the game....")
    score= random.randint(1,62)
    # fetch the higscore
    with open("higscore.txt") as f:
        higscore= f.read()
        if(higscore !=""):
            higscore=int(higscore)
        else:
            higscore =0

    print(f"your score:{score}")
    if(score>higscore):
        # wrote this high score to file 
        with open("higscore.txt" , "w") as f:
         f.write(str(score))
    return score

game()