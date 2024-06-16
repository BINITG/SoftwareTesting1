'''class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
s1=Student("durga",4,55)
print(s1.name,s1.roll,s1.marks)

s2=Student("binit",8,75)
print(s2.name,s2.roll,s2.marks)'''




'''class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("student name:{},roll:{},marks:{}".format(self.name,self.roll,self.marks))
s1=Student("durga",4,55)
s2=Student("binit",8,75)
s1.display()
s2.display()'''





#variables
a=10
class Student:
    cname="durgasoft"
    def __init__(self,name,roll):
        self.name=name
        self.roll=roll
    def m1(self):
        x=40




#how to print docstring.

class Student:
    '''this is student properties and actions'''
    pass
print(Student.__doc__)
help(Student)
print(objectreference.__doc__)





#Example of class

class Student:                                       #creating a class
    def __init__(self):                              #creating a constructor method containing some  variable
        self.name="binit"
        self.roll=10
        self.marks=90
    def talk(self):                                 #creating a method
        print("Hello my name is:",self.name)
        print("my name is :",self.roll)
        print("my marks are:",self.marks)
s1=Student()                                        #creating an object
print(s1.name,s1.roll,s1.marks)                     #By using object reference ,accessing the data.
s1.talk()                                           #calling method


class Test:
    def __init__(self):
        print("constructor execution")
    def m1(self):
        print("method execution")
t1=Test()


#creating a class for employee

class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("emloyee no.:",self.eno)
        print("emloyee name.:",self.ename)
        print("emloyee sal.:",self.esal)
        print("emloyee addr.:",self.eaddr)
e1=Employee(100,"binit",10000,"bihar")
e1.display()

e2=Employee(10,"sony",30000,"bihar")
e2.display()




class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print("emloyee no.:",self.eno)
        print("emloyee name.:",self.ename)
        print("emloyee sal.:",self.esal)
        print("emloyee addr.:",self.eaddr)
e1=Employee(100,"binit",10000,"bihar")
e2=Employee(10,"sony",30000,"bihar")
e3=Employee(1,"mom",50000,"bihar")
e1.display()
e2.display()
e3.display()
print(e1.eno,e1.ename,e1.esal,e1.eaddr)
print(e2.eno,e2.ename,e2.esal,e2.eaddr)
print(e3.eno,e3.ename,e3.esal,e3.eaddr)




class Test:
    def __init__(self):
        self.x=10
t1=Test()
t2=Test()
print(t1.x,t2.x)
t1.x=80
print(t1.x,t2.x)


class Test:
    def __init__(self):
        self.a=1000
        self.b=2000
    def m1(self):
        self.c=3000
        self.d=4000
t1=Test()
t1.m1()
print(t1.a,t1.b,t1.c,t1.d)
t2=Test()
t2.a=8888
t2.b=9999
t2.c=7777
print(t2.__dict__)


#declare instance variable in 3 places:inside costructor,inside instance method,outside class using reference variable

class SE:
    def __init__(self,name,age,tech):
        self.name=name
        self.age=age
        self.tech=tech
s1=SE("durga",48,"python")
s2=SE("murga",40,"kython")
s1.gf1="mallika"
s1.gf2="juhi"
s2.brand1="rc"
s2.brand2="kf"
print(s1.__dict__)
print(s2.__dict__)

#STATIC VARIABLE

class Test():
    a=10
    def __init__(self):
        self.b=20
t=Test()
print(t.a,t.b)
print(Test.a,t.b)



class Test():
    a=10
    def __init__(self):
        self.b=20
        Test.c=30
    def m1(self):
        self.d=40
        Test.e=50
    @classmethod
    def m2(cls):
        cls.f=60
        Test.g=70
    @staticmethod
    def m3():
        Test.h=80
t=Test()
t.m1()
Test.m2()
Test.m3()
Test.i=90
print(Test.__dict__)
print(t.a,t.c,t.e,t.f,t.g,t.h,t.i)
print(Test.a,Test.c,Test.e,Test.f,Test.g,Test.h,Test.i)
# a,c,e,f,g,h,i are static variables while b and d are instance variable.


#how to access static variable.

class Test():
    a=10
    def __init__(self):
        print(self.a)
        print(Test.a)
    def m1(self):
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print(cls.a)
        print(Test.a)
    @staticmethod
    def m3():
        print(Test.a)
t=Test()
t.m1()
t.m2()
t.m3()
print(t.a)
print(Test.a)

#How to modify static variable
class Test:
    a=10
    def __init__(self):
        self.b=20
t1=Test()
t2=Test()
Test.a=888
t1.b=999
print(t2.a,t2.b)
print(t1.a,t1.b)
print(t1.__dict__)
print(t2.__dict__)
