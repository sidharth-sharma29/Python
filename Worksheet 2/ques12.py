'''12. Create a new list from two list using the following condition, Given two list of numbers, write
a program to create a new list such that the new list should contain odd numbers from the first
list and even numbers from the second list.'''
l1=[22,3,14,5]
l2=[33,2,35,7]
l=[]
for i in l1:
    if(i%2!=0):
        l.append(i)
for i in l2:
    if(i%2==0):
        l.append(i)
print(l)