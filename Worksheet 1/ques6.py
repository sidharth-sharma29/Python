'''6. Write a Python program that accepts a sequence of comma-separated numbers from the
user and generates a list and a tuple of those numbers. Sample data : 3, 5, 7, 23  '''

a=input("Enter comma seperated number: ")
L=[]
for i in a:
    if(i!=','):
        L.append(int(i))
T=tuple(L)
print(f"List: {L}\nTuple: {T}")