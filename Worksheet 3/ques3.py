'''3. Write a Python program to reverse a string.'''

def reverse_str(a):
    b=a[::-1]
    return(b)

a=input("Enter a string: ")
print(f"Reverse string: {reverse_str(a)}")