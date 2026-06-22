# d1={}
# print(type(d1))


# # VANNILLA _APPROACHES
# d={1:11,2:21,3:31,4:14,5:51}    #KEY VALUES  ARE UNIQE, AND SHOULDN'T  BE REPEATED
# # print(d[2])

# d[6]=90
# # print(d[6])                # READING EXTRA VALUES FROM KEYBOARD       #

# d[2]=101                     #UPDATING THEEXTRA VALUES FROM THE KEYBPARD
# print(d)



#METHODS_OF _PERFORMING OPERATIONS
a={1:11,2:21,3:31,4:14,5:51}
# a.clear()                              #CLEAR_OPERATION      
# print(a)

# q=a.fromkeys([10,20],55)                #FROMKEYS_OPER4TION
# print(q)

# print(a.get(2))                     #GET_OPERATION
# print(a.items())                    #ITEM_OPERATION         HAVING LIST WITH MULTIPLE TUPLE INSIDE AND EACH TUPLE HAS KEY AND VALUE AS AN ELEMENT

# print(a.keys())                     #KEY_OPERATION
# print(a.values())                   #VALUE_OPERATION


# print(a.pop(1))              #POP_OPERATION              NEEDED TO TELL THE KEY VALUE
# print(a)


# print(a.popitem())             #POP_ITEM _OPERATION     automatically remove last itwem

# print(a.setdefault(22,111))     #SET_DEFAULT_OPERATION                RETURNS THE VALUE OF SPECIFIED KEY THET NOT EXIST EARLIER
# print(a)

# a.update({1:121})              #UPDATE_OPERATION          CAN UPDATE THE VALUE OF EXISTING KEY AND CAN ALSO ADD A NEW KEY-VALUE PAIR
# print(a)



# #TRAVERSING OF LOOPS
# a={1:11,2:21,3:31,4:14,5:51}
# for i in a:
#     # print(i)
#     # print(a[i])
#     print(f"key  {i}: value {a[i]}")