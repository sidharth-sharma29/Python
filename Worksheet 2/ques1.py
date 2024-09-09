'''1. L is a list defined as L= [11, 12, 13, 14].
(i) WAP to add 50 and 60 to L.
(ii) WAP to remove 11 and 13 from L.
(iii) WAP to sort L in ascending order.
(iv) WAP to sort L in descending order.
(v) WAP to search for 13 in L.
(vi) WAP to count the number of elements present in L.
(vii) WAP to sum all the elements in L.
(viii) WAP to sum all ODD numbers in L.
(ix) WAP to sum all EVEN numbers in L.
(x) WAP to sum all PRIME numbers in L.
(xi) WAP to clear all the elements in L.
(xii) WAP to delete L.'''

L= [11, 12, 13, 14]
print(f"original list: {L}")
#1
L.append(50)
L.append(60)
print(L)
#2
L.remove(11)
L.remove(13)
print(L)
#3
L.sort()
print(L)
#4
L.sort(reverse=True)
print(L)
#5
if(13 in L):
    print("13 is present")
else:
    print("13 is not present")
#6
b=len(L)
print(f"Number of element in list = {b}")
#7,8,9
sum=0
sum_even=0
sum_odd=0
for i in L:
    sum+=i
    if(i%2==0):
        sum_even+=i
    else:
        sum_odd+=i
print(f"sum of all elements in list = {sum}\nsum of odd elements = {sum_odd}\nsum of even elements = {sum_even}")
#10
prime=0
for i in L:
    bool=1
    for z in range(2,i):
        if(i%z==0):
            bool=0
            break
    if(bool==1):
        prime+=i
print(f"sum of prime no in list = {prime}")
#11,12
L.clear()
print(L)
del(L)
