import random #random is a module and import is a statement
import logo_art # pyright: ignore[reportMissingImports]
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen): #this is the way of defining a fuction
    if (level_chosen=='easy'):
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS
    
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("Your answer is too low")
        return attempts-1
    elif guessed_number>answer:
        print("Your number is too high")
        return attempts-1
    else:
        print(f"you are correct!! your  answer is {answer}")

print(logo_art.logo)
print("Let me think of a number between 1 to 50")
answer = random.randint(1,50)#so randint() is a function 
print(answer)
level=input("Choose level of difficulty... type 'easy' or 'hard':")
attempts= set_difficulty(level)
guessed_number=0
while guessed_number!=answer:
    print(f"Your total attempts are {attempts}.")#to enter variable inside string 
    guessed_number = int(input("Guess a number:"))
    attempts=check_answer(guessed_number,answer,attempts)
if attempts==0:
    print("You are out of attempts")
    
elif guessed_number != answer:
    print("Try again")


