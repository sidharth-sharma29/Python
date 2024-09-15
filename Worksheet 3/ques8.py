'''8. Define a Python function student(). Using function attributes display the names of all
arguments.'''

def student(a,b,c):
    print(f'''student_name: {a}
class: {b}
roll_no.: {c}''')
    
a=input("Enter name: ")
b=int(input("Enter class: "))
c=int(input("Enter roll_no.: "))
student(a,b,c)