'''6. S1 is a set defined as S1= [10, 20, 30, 40, 50, 60]. S2 is a set defined as S2= [40, 50, 60, 70, 80,
90].
(i) WAP to add 55 and 66 in Set S1.
(ii) WAP to remove 10 and 30 from Set S1.
(iii) WAP to check whether 40 is present in S1.
(iv) WAP to find the union between S1 and S2.
(v) WAP to find the intersection between S1 and S2.
(vi) WAP to find the S1 - S2.'''

S1= {10, 20, 30, 40, 50, 60}
S2= {40, 50, 60, 70, 80,90}
print(f"Original set\nS1 = {S1}\nS2 = {S2}")
#1
S1.add(55)
S1.add(66)
print(f"S1: {S1}")
#2
S1.discard(10)
S1.discard(30)
print(f"S1: {S1}")
#3
if(40 in S1):
    print("40 is present")
else:
    print("40 is not present")
#4
a=S1.union(S2)
print(f"union of S1 and S2: {a}")
#5
b=S1.intersection(S2)
print(f"intersection of S1 and S2: {b}")
#6
b=S1.difference(S2)
print(f"S1-S2: {b}")

