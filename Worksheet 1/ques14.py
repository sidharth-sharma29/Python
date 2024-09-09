'''14. Given a positive integer N, the task is to write a Python program to check if the number
is Prime or not in Python.'''

a=int(input("Enter a number: "))
b=0
for i in range(2,a):
    if(a%i==0):
        b=1
        break
if(b==0):
    print("Prime no")
else:
    print("not a prime number")