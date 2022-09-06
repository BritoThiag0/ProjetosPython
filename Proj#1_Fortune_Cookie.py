#Projeto 1
#Projeto de um biscoito da sorte digital.
#Diz uma frase e um número da sorte aleatoriamente.

import random as r

lucky_num = r.randint(1, 100)
fortune_num = r.randint(1, 3)
fortune_text = ""

if fortune_num == 1:
    fortune_text = "You'll have a great day!"
elif fortune_num == 2:
    fortune_text = "Today will tough...but worth it!!"
elif fortune_num == 3:
    fortune_text = "You'll get married next year!!!"

print(f"{fortune_text} Your lucky number is: {lucky_num}")