'''1. Write a Python program to calculate the difference between a given number and 17
with the help of function. If the number is greater than 17, return twice the absolute
difference.'''

def diff(x):
    if(x>17):
        return f"Twice the absolute difference between the entered number and 17 = {2*abs(x-17)}"
    else:
        return f"Absolute difference between the entered number and 17 = {abs(x-17)}"
    
a=int(input("Enter the number: "))
print(diff(a))