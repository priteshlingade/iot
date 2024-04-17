num=int(input("enter 4 digit number"))

def face(n):
    while n>0:
        fac=int(n%10)
        n=int(n/10)
        print(fac)


def place(num):
    unit=num/10
    tense=num/100
    hund=num/1000
    thou=num/10000
    print(unit)
    print(tense)
    print(hund)
    print(thou)
    
def rev(n):
     while n>0:
        fac=int(n%10)
        n=int(n/10)
        

face(num)
place(num)

