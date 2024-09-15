'''5. Write a Python function that takes a list and returns a new list with distinct elements
from the first list.'''

def distinct(a):
    c=set(a)
    b=list(c)
    return f"List with distinct elements: {b}"

w=int(input("Enter number of elements in list: "))
l=[]
idx=0
for i in range(w):
    q=int(input(f"Enter element at index {idx}: "))
    l.append(q)
    print()
    idx+=1
print(f"Entered list: {l}")
print(distinct(l))