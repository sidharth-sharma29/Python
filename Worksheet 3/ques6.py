'''6. Write a Python program to print the even numbers from a given list. Sample List : [1,
2, 3, 4, 5, 6, 7, 8, 9] Expected Result : [2, 4, 6, 8]'''

def even(a):
    l=[]
    for i in a:
        if(i%2==0):
            l.append(i)
    return f"List with Even Elements: {l}"

w=int(input("Enter number of elements in list: "))
l=[]
idx=0
for i in range(w):
    q=int(input(f"Enter element at index {idx}: "))
    l.append(q)
    print()
    idx+=1
print(f"Entered list: {l}")
print(even(l))