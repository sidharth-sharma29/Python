'''5. D is a dictionary defined as D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}.
(i) WAP to add new entry in D; key=8 and value is 8.8
(ii) WAP to remove key=2.
(iii) WAP to check weather 6 key is present in D.
(iv) WAP to count the number of elements present in D.
(v) WAP to add all the values present D.
(vi) WAP to update the value of 3 to 7.1.
(vii) WAP to clear the dictionary.'''
#1
D= {1:5.6, 2:7.8, 3:6.6, 4:8.7, 5:7.7}
print(f"Original dictionary: {D}")
D.update({8:8.8})
print(D)
#2
D.pop(2)
print(D)
#3
if(6 in D):
    print("key 6 is present")
else:
    print("key 6 is not present")
#4
count=len(D)
print(f"no of element in D = {count}")

#5
sumval=0
for i in D:
    sumval+=D[i]
print(f"The sum of values of D = {sumval}")
#6
D.update({3:7.1})
print(D)
#7
D.clear()
print(D)