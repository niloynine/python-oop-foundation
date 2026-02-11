
class Employ:#class
    num_of_employee=0#class variable
    raise_amount=1.04
    def __init__(self,first,last,pay):#constructor
        self.first=first#instance variable
        self.last=last#instance variable
        self.email=first+'.'+last+'@gmail.com'#instance variable
        self.pay=pay#instance variable
        Employ.num_of_employee+=1#class variable increase by 1 when a new employee is created
    def fullname(self):#instance method
        return '{} {}'.format(self.first,self.last)#instance method can access instance variable and class variable
        
    def apply_raise(self):#instance method
        self.pay=int(self.pay*self.raise_amount)#instance method can access instance variable and class variable
        
        
print(Employ.num_of_employee)
emp_1=Employ('Ayesha','Mahmud',80000)#object of the class
emp_2=Employ('Niloy','Mutsuddy',80000)#object of the class
print(Employ.num_of_employee)#class variable can be accessed by the class name and instance name
print(emp_1.email)#instance variable can be accessed by the instance name
print(emp_2.email)

print(emp_1.fullname())#instance method can be accessed by the instance name
print(emp_1.pay)
emp_1.apply_raise()#instance method can be accessed by the instance name
print(emp_1.pay)