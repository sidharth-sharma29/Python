'''12. Write a Python class that has two methods: get_String and print_String , get_String
accept a string from the user and print_String prints the string in upper case.'''

class string:

    def get_string(self,a):
        self.r=a
    def print_string(self):
        c=self.r.upper()
        print(c)

strc=input("Enter string: ")
a=string()
a.get_string(strc)
a.print_string()