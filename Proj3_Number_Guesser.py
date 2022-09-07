#Projeto 3
#Jogo de adivinhação de um número
import random
import time

print("""Hi! Welcome to the Gussing Game.
Please guess a number between 1 and 100.""")
time.sleep(3)
guess = int(input("What is your guess? "))
print("Doing the magic...")
time.sleep(5)
correct_num = random.randint(1, 100)
guess_count = 0

while guess != correct_num:
    guess_count += 1
    
    if guess < correct_num:
        guess = int(input("Wrong. You need to guess higher. What is your guess? "))
    elif guess > correct_num:
        guess = int(input("Wrong. You need to guess lower. What is your guess? "))
    
    

print("You got the rigth answer!!! :)")
print(f"It only took you {guess_count} guesses.")