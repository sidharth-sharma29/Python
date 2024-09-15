'''2. Write a Python program for a function. to test whether a number is within 100 to 1000
or 2000.'''

def check(a):
    if(a>=0 and a<100):
        return "0 <= a < 100"
    elif(a>=100 and a<1000):
        return "100 <= a < 1000"
    elif(a>=1000 and a<2000):
        return "1000 <= a < 2000"
    else:
        return "Out of range"

a=int(input("Enter a: "))
print(check(a))
