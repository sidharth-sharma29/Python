'''7. Write the following program.
(i) WAP to print 100 random strings whose length between 6 and 8.
(ii) WAP to print all prime numbers between 600 and 800.
(iii) WAP to print all numbers between 100 and 1000 that are divisible by 7 and 9'''
#1
import random as rd
for i in range(100):
    a=rd.randint(6,8)
    for j in range(a):
        b=rd.choice([65,97])
        c=rd.randint(b,b+25)
        print(chr(c),end="")
    print()
print()
#2
print("Prime numbers between 600 and 800:")
for i in range(600,801):
    bool=1
    for j in range(2,i):
        if(i%j==0):
            bool=0
            break
    if(bool==1):
        print(i,end=" ")

print()
print()
#3
print("all numbers between 100 and 1000 that are divisible by 7 and 9")
for i in range(100,1001):
    if(i%7==0 and i%9==0):
        print(i,end=" ")
