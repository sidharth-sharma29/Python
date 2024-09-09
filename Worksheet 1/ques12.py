'''12. Write a program that take a user input of three angles and will find out whether it can
form a triangle or not.'''

a=float(input("Enter first angle: "))
b=float(input("Enter second angle: "))
c=float(input("Enter third angle: "))
if(a+b+c==180 and a!=0 and b!=0 and c!=0):
    print("Form a triangle")
else:
    print("Not form a triangle")