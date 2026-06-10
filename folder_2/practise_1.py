# l=[3,-1,4,-5,9]
# positv = []
# neg = []
# for i in range(0,len(l)):

#     # print(f"{i} ={l[i]}") 
#     #                                   #TO SEPARATE POSITIVE AND NEGATIVE VALUES 

#     if l[i]>=0:
#         positv.append(l[i])
#     else:
#         neg.append(l[i])    
# print(positv)
# print(neg)        

# c=0
# l=[1,2,3,4,5]
# # print(len(l))    #FINDIMNG MEAN OF LIST
# for i in l:
#     c=c+i
# print(c/len(l))    


# l=[5,3,8,32,1,9]
# # l.sort()
# # print(l[-1])
# large=0
# index=0
# for i in range(len(l)):     #FINDING INDEX OF HIGHESRTNO, IN A LIST
#     if l[i]>large:
#         index=i
#         large=l[i]
# print(f"highest number{large} at index {index}")



# l=[5,3,8,32,1,9]
# # l.sort()
# # print(l[-1])
# large_1=0
# large_2=0
# index=0
# for i in l:
#     if i>large_1:   
#         large_2=large_1
#         large_1=i
#     elif i>large_2:
#         large_2=i

# #for i in range(len(l)):     #FINDING INDEX OF HIGHESRTNO, IN A LIST
#     # if l[i]>large_1:
#     #     large_2=large_1
#     #     large_1=l[i]
# print(f"  SECOND  highest number  {large_2} ")


a=[1,3,14,5,67,402]
srot=0
for i in a:
    if i>i+1:
        print("not sorted")
        break
else:
        print("sorted")

#     if i-1<i:
#      srot+=1
# if srot ==len(a):
#      print("sorted")            