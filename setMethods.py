"""
myset = {2,2,4,6,7,8}


myset.add(10)


#myset.remove(7)
#myset.discard(13)
myset.pop()


print(myset)
"""
"""
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

AUB = A.union(B)
AIB = A.intersection(B)
ADB = A.difference(B)
ASB = A.symmetric_difference(B)



print(A.intersection_update(B))
print(f"Set A: {A}")
print(f"Set B: {B}")
"""


A = {10,20,30,40,50,60}
B = {30,40,50,70,80}
C = {40,50,80,90,100}



"""
=> Find elements common to all three sets.
        ((A ^ B) ^ C)
"""

print(A & B & C)

"""
=> Find elements present in exactly two sets.
        ((A ^ B) - C) U ((A ^ C) - B) U ((B ^ C) - A)
"""
print(((A & B) - C) | ((A & C) - B) | ((B & C) - A))


"""
=> Find elements that apears in only one set.
        (A - (BUC)) U (B - (AUC)) U (C - (AUB))
"""
print((A - (B | C)) | (B - (A | C)) | (C - (A | B)))


"""
=> Find all unique elements across the three sets.
        ((AUB) U C)
"""
print(A | B | C)






















