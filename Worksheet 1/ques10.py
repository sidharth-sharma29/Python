'''10. Write a program that will tell whether the given year is a leap year or not.'''
a=int(input("Enter year: "))
if (a%400 == 0) or (a%4==0 and a%100!=0):
    print(f"{a} is a Leap Year")
else:
    print(f"{a} is not a Leap Year")