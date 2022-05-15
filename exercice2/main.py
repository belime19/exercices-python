a=input("Donne deux mots séparrés par un espace :")
resultat = False
mot1,mot2=a.split(" ")
if(len(mot1) != len(mot2)):
    print(resultat)
else:
    i=0
    while (i<len(mot1)):
        if(str(mot1).count(mot1[i]) != str(mot2).count(mot2)):
            print(resultat)
            break
        i+=1
    if(i==len(mot1)):
        print("True")