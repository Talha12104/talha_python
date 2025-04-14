import random

def game():
    print("You are Playing game")
    score = random.randint(1,100)
    with open("hiScore.txt") as f:
        hiScore = f.read()
        if (hiScore != ""):
            hiScore = int(hiScore)
        else:
            hiScore = 0
        print(f"Your Score {score}")
    with open("hiScore.txt", "w") as f:
        if (hiScore < score):
            f.write(str(score))
            
        return score

game()