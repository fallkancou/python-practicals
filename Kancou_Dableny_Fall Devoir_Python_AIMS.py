def somme(n):
        l=[]
        i=0
        for i in range(0,n):
                s=i+3
                l.append(s)
                i=i+1
        print(l)
        print(sum(l))


def produit(n):
        L=[]
        l=[]
        i=0
        pr=1
        for i in range(0,n):
                s=i+3
                l.append(s)
                i=i+1
        print(l)
        for j in range(0,len(l)):
                pr*=l[j]
                j=j+1
                L.append(pr)
        print(L)
        print(pr)

def semaine(n):
        L=['lundi','mardi', 'mercredi','jeudi','vendredi','samedi','dimanche']
        for i in range(0,len(L)):
                if i<=4 and n==i:
                        jour=L[i]
                        print("Aujourd'hui c'est", jour)
                elif i>4 and n==i :
                        print("C'est le weekend")


def nom():
        l=['fall']
        for i in range(0,len(l)):
                nm=l[i]*3
                print(nm)

def nom1():
        i=0
        l=['fall']
        while i<= len(l):
                nm=l[i]*3
                print(nm)
                break

def Fibonacci(n):
    l= input("donner la condition initiale de la suite\n")
    L1=[int(l[i]) for i in range(len(l))]
    a0,a1= L1[0],L1[1]
    print(L1)
    i=0
    while i<=n-1:
        a0,a1=a1,(a0+a1)
        i=i+1
        L1.append(a1)
    return L1


def sequence(n):
    l= input("donner la condition initiale de la suite\n")
    L1=[int(l[i]) for i in range(len(l))]
    x0,x1= L1[0],L1[1]
    print(L1)
    i=0
    while i<=n-1:
        x0,x1=x1,(1/2*((6*int(x0))+int(x1)))
        i=i+1
        L1.append(x1)
    return L1

        
                        



        
        
