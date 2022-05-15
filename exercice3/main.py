import random

secret = random.randint(0,100)
essai=0
while essai<10:
    valeur=int(input("deviner le secret: "))
    if secret < valeur:
        print("Trop grand")
    elif secret > valeur:
        print("Trop petit")
    else:
        print("Gagné en {} essais !".format(essai+1))
    essai+=1
if essai == 10:
    print("Perdu ! Le secret était {}".format(secret))
