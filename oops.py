'''class student:
    name='ram'
    age=20

s1=student()
s2=student()
s1.name="ramu"
s2.name="raju"
print(s1.name)
print(student.name)
print(s2.name)
print(student.name)'''


'''class college:
    name='gopalan university'
    loc='hoodi' 

    def __init__(self,name,age,dept):
        self.name=name
        self.age=age
        self.dept=dept
    def access(self):
        print(self.name,self.age,self.dept)
s1=college("ram",21,"ISE")
s1.access()   



def display(self):
    print(self.name,self.age,self.dept)
def change_name(self,new):
    self.name=new

s1=college("raju",20,"cse")
s2=college("ramu",20,"ise")
print("before")
s2.display()
s2.change_name("rama")
print("after")
s2.display()
print('-------------')
college'''

'inheritance'

'''class A:
    a=10
class B(A):
    b=20
ob1=B()
print(ob1.a,ob1.b)'''


class Bank:
    bname='sbi'
    bloc='BSVN'

    def __init__(self,name,phno,eid):
        self.name=name
        self.phno=phno
        self.eid=eid
    def display(self):
        print(self.name,self.phno,self.eid)

c1=Bank("harika",9876543209,'you123@gmail.com')       
class bank_details(Bank):
    founder='Sairam'

    def __init__(self, name, phno, eid, add, pan):
        super().__init__(name, phno, eid)
        self.add = add
        self.pan = pan

    def display(self):
        super().display()
        print(self.add,self.pan)

c1=bank_details("harika",9876543209,'you123@gmail.com','hoodi','asdfhg12345')
c1.display()    







  