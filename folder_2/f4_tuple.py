# a=("hello",123)
# print(type(a))

# a=["sdfg",123]
# print(type(a))
# tuo=tuple(a)
# print(type(tuo))
# print(tuo[0])


# a=("hello","ganesha","kya kar rhe ho",1,2,1,1,1,1,1,1,3,7,9)
# print(a.index("hello"))
# print(a.count(1))

# a=1,2,3,4,5
# print(type(a))          #ALSO A TUPLE

#PACKING AND UNPACKING OF TUPLE

def students():
    return "ram",11,"kumarram@gmail.com"
info = students()
print(info)
print(students())

name,age,email = info
print(name)