n=int(input("entrer une valeur naturelle: "))
i=1
while i<n+1:
    m=n+1-i
    print(" "*(n-i)+str(m%10)*i)
    i+=1