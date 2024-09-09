'''15. Given a positive integer N. The task is to find 1**2 + 2**2 + 3**2 + ..... + N**2'''

a=int(input("Enter number n = "))
sum=0
for i in range(1,a+1):
    sum+=i**2
print(f"1**2 + 2**2 + 3**2 + ..... + N**2 = {sum} (when n={a})")