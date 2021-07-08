#   A = [‘a’,’b’,’c’,’d’] B = [‘1’,’a’,’2’,’b’]
#   Find a intersection b and a union b

import math

# declaring the function
def Union(A,B):
    result = list(set(A) | set(B))  # | it is or operator it adds the list since we cannot
    return result                   # add the sets



# finding the intersection of list a and b

def Intersection(A,B):
    result_1 = list(set(A) & set(B))
    return result_1


A = ['a','b','c','d']
B = ['1','a','2','b']
print("Union is : ",Union(A,B))
print("Intersection between A and B is: ", Intersection(A,B))


