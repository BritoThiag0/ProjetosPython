# Projeto 4
# Desenvolvimento de um timer com Python

import time

run = input("Strat? (Answer yes or no)\n>>")

seconds = 0

if (run == "yes" or run == "Yes"):
    while seconds != 10:
        print("\t>", (seconds + 1))
        time.sleep(1)
        seconds += 1
    print("Time's up!!!")
else:
    print("Please answer yes or no.")
