# n= int(input("enter n:")) 
# n=str(n)
# for i in range(len(n)):
#     print(n[i])

# n= int(input("enter n:")) 
# r=0
# while n!=0:
#     r=n%10
#     n=n/10
#     print(r)
# while n!=0:
#     print(n%10)
#     n=n//10
 

# n= int(input("enter n:"))   #reverse of num
# ans=0
# rem=0
# while n>0:                    #METHOD_1
#     rem=n%10
#     n=n//10
#     ans=ans*10+rem
# print(ans)


# n= int(input("enter n:"))      #reverse of num
# ans=0
# while n>0:                      #METHOD_2
#     ans=ans*10+n%10
#     n=n//10
# print(ans)


# n= int(input("enter n:"))      #palindrone of num
# ans=0
# orignal=n
# while n>0:                     
#     ans=ans*10+n%10
#     n=n//10
# if orignal==ans:
#     print("palin")    
# else:
#     print("no")