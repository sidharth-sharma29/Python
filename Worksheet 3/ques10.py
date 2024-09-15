'''10. Write a Python class named Student with two instances student1, student2 and assign
values to the instances' attributes. Print all the attributes of the student1, student2
instances with their values in the given format.'''

class student:
    def __init__(self,a,b):
        self.stu_name=a
        self.stu_id=b
    def display(self):
        print(f'''Student_Name: {self.stu_name}
Student_ID: {self.stu_id}''')

student1=student("abc",123)
student2=student("def",456)
print("Student1: ")
student1.display()
print("\nStudent2: ")
student2.display()