'''9. Iterate the given list of numbers and print only those numbers which are divisible by 5.'''

a=int(input("Enter number of element in list: "))
l=[]
idx=1
for i in range(a):
    b=int(input(f"Enter element {idx} = "))
    l.append(b)
    idx+=1
print(l)
print("numbers in list which are divisible by 5")
for i in l:
    if(i%5==0):
        print(i,end=",")