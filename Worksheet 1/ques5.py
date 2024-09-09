'''5. Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5'''

n=int(input("Enter integer n = "))
a=n*10+n
b=n*100+n*10+n
print(f"Value of n+nn+nnn = {n}+{a}+{b} = {n+a+b}")