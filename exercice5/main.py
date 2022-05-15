import math

def sum(n):
    result=0
    for i in range(1,n+1):
        result+=1/(i**2)
    return result

for n in range(1,10001):
    err=abs(sum(n)-(math.pi**2)/6)
    print("{}   {}  {}".format(n,sum(n),err))