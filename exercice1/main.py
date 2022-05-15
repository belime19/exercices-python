resulat= "Les entiers divisible par 3 sont: "
for i in range(10):
    entier=int(input("Entrer un entier:"))
    if entier%3 == 0:
        resulat+= str(entier)+", "
print(resulat)