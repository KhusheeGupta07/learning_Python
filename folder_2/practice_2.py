# #MERGE TWO DICTIONARIES INTO ONE
# d1={1:50,2:52}
# d2={3:50,5:66}

# # d1.update(d2)         #INBUILT METHOD
# # print(d1)

# for i in d2:          #BY LOGICIC BILDING
#     # print(i)
#     # print(d2[i])
#     d1[i]=d2[i]
# print(d1)    


# #SUM OF A DICTIONARY
# d={"a":1,"b":2}
# sum=0
# for i in d:
#     sum += d[i]
# print(sum)


#COUNT FREQUENCY OF EACH ELEmNT OF LIST USING DICTIONARY
# l=["a","b","c","c","a","a","a","a","a","c"]               #GOOD_QUESTION
# d={}
# for i in l:
#     if i in d.keys():
#         d[i]+=1
#     else:
#         d[i]=1    
# print(d)        

#COMBIME TWO DICTIONARIERS AND ADDING VALUES FOR THE COMMON KEYS
d1={1:50,2:52,4:33}
d2={4:22,3:50,5:66}
for i in d2: 
    if i in  d1.keys():  #BY LOGICIC BILDING
       d1[i]= d1[i] + d2[i]
    else:
        d1[i]=d2[i]
  
print(d1)  