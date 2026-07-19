# instanse method capture thre location of the object and  class method capture the location of class


# class animal:
#     a=12                                   #class attribute

#     def __init__(self,name):
#         print("hello my shiva")
#         self.name = name                 # <----- object/instancee attribute  as this self.name is also a variable.

#     def intro(self):
#         print(f"radhe krishna ,, vse this is {self.name}")          # instance/object method

#     @classmethod                         #YE CLASS METHOD H ,BUT  ISE HM OBJECT K THROUGH BHI CALL KR SKTE H,,, YEH JO PARAMETER H "CLS" YE ORIGINAL  CLASS KI LOCATION KO CAPTURE KREGA.
#     def details(cls):
#         print("take care")

#                         #THIS OBJECT(OBJJ) CAN CALL THE  INSTANCE METHOD.
#                          #AS INSTANCE METHOD capture thre location of the object



# objj = animal("lion") 
#objj.intro()
#print(objj.name)



# class animal:
#     a=12                                   #class attribute

#     def __init__(self,name):
#         print("hello my shiva")
#         self.name = name                 # <----- object/instancee attribute  as this self.name is also a variable.

#     def intro(self):
#         print(f"radhe krishna ,, vse this is {self.name}")          # instance/object method

#     @classmethod                         #YE CLASS METHOD H ,BUT  ISE HM OBJECT K THROUGH BHI CALL KR SKTE H,,, YEH JO PARAMETER H "CLS" YE ORIGINAL  CLASS KI LOCATION KO CAPTURE KREGA.
#     def details(cls):
#         print("take care")
# objj = animal("lion") 
# objj.details()



# class animal:
#     a=12                                   #class attribute

#     def __init__(self,name):
#         print("hello my shiva")
#         self.name = name                 # <----- object/instancee attribute  as this self.name is also a variable.

#     def intro(self):
#         print(f"radhe krishna ,, vse this is {self.name}")          # instance/object method

#     @classmethod                         #YE CLASS METHOD H ,BUT  ISE HM OBJECT K THROUGH BHI CALL KR SKTE H,,, YEH JO PARAMETER H "CLS" YE ORIGINAL  CLASS KI LOCATION KO CAPTURE KREGA.
#     def details(self,cls):
#         print(f"take care , my dear {self.name}")

                                #but this time this object(objj) is not able to call the class method 
                                # ',AS  class method capture the location of class
                                
# objj = animal("lion") 
# objj.details()


# class animal:
#     a=12                                   #class attribute

#     def __init__(self,name):
#         print("hello my shiva")
#         self.name = name                 # <----- object/instancee attribute  as this self.name is also a variable.

#     def intro(self):
#         print(f"radhe krishna ,, vse this is {self.name}")          # instance/object method

#     @classmethod                        
#     def details(clfs):                          #CLASSMETHOD
#         print(f"take care,, you are just a {clfs.a} year old child")
# objj = animal("lion") 
# objj.intro()
# objj.details()




class animal:
    a=12                                   #class attribute

    def __init__(self,name):
        print("hello my shiva")
        self.name = name                 # <----- object/instancee attribute  as this self.name is also a variable.

    def intro(self):
        print(f"radhe krishna ,, vse this is {self.name}")          # instance/object method

    @classmethod                        
    def details(cls):
        print("take care")


    @staticmethod
    def speak() :
        print("hello, how are you my dear kanha")   
objj = animal("lion") 
objj.speak()