'''7. Write a Python program to access a function inside a function.'''

def sqr(x):
    return x**2
def sumofsqr(y,z):
    return f"{y}**2 + {z}**2 = {sqr(y)+sqr(z)}"

print("given equation: a**2+b**2")
a=int(input("Enter a = "))
b=int(input("Enter b = "))
print(sumofsqr(a,b))