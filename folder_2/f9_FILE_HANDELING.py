# open("handmade.txt","x")            #CREATING A FILE           

# f=open("handmade.txt","w")            #WRITING INSIDE A FILE
# data= input("write your thoughts")
# f.write(data)



# file = open("handmade.txt","r")           #READING INSIDE A FILE
# print(file.read())



# file = open("python_2/f3_list.py","r")     

# #F3 WALI FILE KO READ KRNE K LIYE PHLE USE PYTHON 2 SE NIKALKR PYHON DIRECTORY M SHIFT KRO,, 
# # 
# # ydi ""python_2/"" yeh ni laga rhe ho toh

# print(file.read())

# f=open("handmade.txt","a")
# dataa = input("nyer the content u wnat:--")           #APPEND
# print(f.write(dataa))

#USE OF WITH OPEN_KEYWORD
with open("handmade.txt","a") as f:
    f.write("" +"MY NAME IS HARI")