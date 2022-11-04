from re import A


def Fib(x):
    if (x==0) :
        return 0
    elif(x==1):
        return 1
    else:
        return Fib(x-1) + Fib(x-2)

def factorial(x):
    i=0
    h=1
    f=x
    while (i !=x):
        h= h * f 
        f= f-1
        i = i + 1
    return h


List = [[1,2],[3,4],[5,6]]
List2= []

for elemento in List:
    a= Fib(elemento[0])
    b= factorial(elemento[1])
    List2.append([a,b])

print (List2)





