import random

def set_difficulty(level_chosen):
    if level_chosen=="easy":
        attempts=10
    else:
        attempts=5
def check_answer(guessed_answer,answer,attempts):
    if(guessed_answer<answer):
        print("Your guess is too low.")
    elif(guessed_answer>answer):
        print("Your guess is too high.")
    else:
        print("Your answer is right.")

def game():
    print("Let me think of a number between 1 to 50.")
    answer=random.randint(1,50)
    
    level=input("Choose level of difficulty('easy'or 'hard'):")
    attempts=set_difficulty(level)
    guessed_answer=0
    while (guessed_answer!=answer):
        print(f"You have {attempts} attempts left to guess the answer")
        guessed_answer=int(input("Guess a number:"))
        attempts=check_answer(guessed_answer,answer,attempts)
        if(attempts==0):
            print("You lose the game..")
            return
        elif(guessed_answer==answer):
            print("Guess again!")


EASY_LEVEL_ATTEMPTS=8
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
    
def check_answer(guessed_answer,answer,attempts):
    if(guessed_answer<answer):
        print("Your guess is too low.")
        return attempts-1
    elif(guessed_answer>answer):
        print("Your guess is too high.")
        return attempts-1
    else:
        print("Your answer is right.")

def game():
    print("Let me think of a number between 1 to 50.")
    answer=random.randint(1,50)
    
    level=input("Choose level of difficulty('easy'or 'hard'):")
    attempts=set_difficulty(level)
    guessed_answer=0
    while (guessed_answer!=answer):
        print(f"You have {attempts} attempts left to guess the answer")
        guessed_answer=int(input("Guess a number:"))
        attempts=check_answer(guessed_answer,answer,attempts)
        if(attempts==0):
            print("You lose the game..")
            print("Correct answer is:", answer)
            return
        elif(guessed_answer==answer):
            
            print("Want to play again!!")
game()