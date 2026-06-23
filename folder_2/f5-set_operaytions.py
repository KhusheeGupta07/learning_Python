#ADD OPERATION
s={1,2,3,4,5}
# s.add(9)                 #TO ADD AN ELEMENT I  SET WHICH IS DIFFERENT FROM THE OLD ONES
# print(s)

#clEAR OPERATION
# s.clear()
# print(s)          #VSE TO EMPTY SET BNA NI SKTE AS VO DICTIONARY BN JAYEGA, TOH THIS IS METHOD

#DISCARD OPERATION
# s.discard(3)            #TO REMOVE A SPECIFIC ELEMENT FROM THE SET
# print(s)

#POP 
# s.pop()                                 ##TO REMOVE A RANDOM ELEMENT FROM THE SET
# print(s)

#DIFFERENCE
s1={2,3,4,5,6}
s2={5,6,7,8,9}
# print(s1.difference(s2))
# print(s1-s2)
# print(s2-s1)

# print(s2)


# s2-=s1
# print(s2)

#INTERSECTION 
# print(s1.intersection(s2))
# print(s1&s2)

#subset
s3={6,7}
s4={2,5,6}
# print(s3.issubset(s2))
# print(s3<=s2)               #CHECKING SUBSET
# print(s4<=s2)

# print(s2.issuperset(s3))
# print(s2>=s3)                               #CHECKING SUPERSET


#   SYMMETRIC_DIFEERNCE
# print(s1.symmetric_difference(s2))
# print(s1^s2)

#UNION_OPERATOR
print(s1 |s2)
