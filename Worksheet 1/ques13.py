'''13. WAP to find compound interest for given values.'''

p=float(input("Enter principle ammount: "))
r=float(input("Enter interest rate: "))
t=float(input("Enter time period in years: "))
n=float(input("Enter number of times interest applied per time period: "))

a=p*((1+r/n)**(n*t))
print(f"Compound Interest = {a-p}")