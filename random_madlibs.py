import random 

def guess(x):
    random_number = random.randrange(1, x)
    lives = 7
    
    while lives > 0:
        guess = input(f"Enter a number between 1 and {x}: ")
        if guess == random_number:
            print (f"Congrats, you have guessed {random_number} correctly")
            break
        elif guess < random_number:
            lives -= 1
            print("Sorry, too low, try again")
            print("%d lives left!"%lives) #needed for string formatting
        elif guess > random_number:
            lives -= 1
            print("Sorry, too high, try again")
            print("%d lives left!"%lives) #needed for string formatting
    
    if lives == 0:
        print(f"Game over, sorry the number was {random_number}")
    
   
guess(20)

