import math as m
import random as r
alpha = "abcdefghijklmnopqrstuvwxyz"
number = '1234567890'
signs = '`~!@#$%^&*()_+-={}[]\'\"\:;<>,.?/'
bigl = [alpha,number,signs]
def ind(n):
    half = m.ceil(n/2) 
    dhalf = m.floor(half/2)
    first = r.randint(dhalf,half)
    ddhalf = m.ceil((n-first)/2)
    second = r.randint(dhalf,ddhalf)
    third = n-(first+second)
    return list((first,second,third))

def shuff(inds):
    rinds = []
    for i in range(len(inds)):
        a = r.choice(inds)
        rinds.append(a)
        inds.remove(a)
    return rinds
def password(nn):
    inds = shuff(ind(nn))
    string = ''
    for thing in bigl:
        n = inds[bigl.index(thing)]
        for i in range(n):
            letter = r.choice(thing)
            aa = r.randint(0,1)
            if aa == 1:
                letter = letter.upper()
            string += letter
    l = list(string)
    r.shuffle(l)
    password = ''.join(l)
    return(password)
print("Password Generator!")
while True:
    length = int(input("length of the password?:"))
    print(password(length))
    inp = input("Do you want to go again? Y/n:")
    inp = inp.lower()
    if inp == "n":
        break
