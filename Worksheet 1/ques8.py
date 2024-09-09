'''8. User will input (2numbers). Write a program to swap the numbers. Add incrementally
in any one variable.'''

a=int(input("Enter first number a = "))
b=int(input("Enter second number b = "))
a=a+b
b=a-b
a=a-b
print(f"After swaping a = {a} and b = {b} ")
b=b+a
print(f"b = {b}")