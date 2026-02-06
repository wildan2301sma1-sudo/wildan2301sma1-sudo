class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age 
        
    def myfunc(abc):
         print("Hello My Name Is " + abc.name)
    
p1 = Person("John", 36)
p1.myfunc()