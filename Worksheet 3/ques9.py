'''9. Write a Python class named Student with two attributes: student_id, student_name. Add
a new attribute: student_class. Create a function to display all attributes and their values
in the Student class.'''

class student:
    student_id=2323
    student_name="abc"
    
    def display(self):
        print(f'''Student_Name: {self.student_name}
Student_ID: {self.student_id}
Student_cgp: {self.cgp}''')
        
a=student()
a.cgp=10
a.display()
