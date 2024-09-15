'''4. Write a Python function that accepts a string and counts the number of upper and lower
case letters.'''

def cnt(a):
    uct=0
    lct=0
    for i in a:
        if(i.isupper()==True):
            uct+=1
        elif(i.islower()==True):
            lct+=1
    return f"Upper cases: {uct}\nLower cases: {lct}"

a=input("Enter string: ")
print(cnt(a))