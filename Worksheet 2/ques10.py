'''10. Write a Python program to check if a given number is even or odd using boolean variables.'''

a=int(input("Enter number : "))
bool=True
if(a%2==0):
    bool=False
if(bool==True):
    print("Odd number")
else:
    print("Even number")