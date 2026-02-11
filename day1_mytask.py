class student:
    ts=0
    def __init__(self,name,roll,dept,sub1,sub2,sub3):
        self.name=name
        self.roll=roll
        self.dept=dept
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        student.ts+=1
        
    def cal_avg(self):
        self.avg= ((self.sub1 + self.sub2 + self.sub3) / 3)
        
    def get_grade(self):
        if self.avg>=80:
            self.grade='A'
        elif self.avg>=70:
            self.grade='B'
        elif self.avg>=60:
            self.grade='C'
        else:
            self.grade='F'
        
    def display_info(self):
        print("name- ", self.name)
        print("roll- ", self.roll)
        print("avg mark- ", self.avg)
        print("grade- ", self.grade)
        
        
print("total stu-",student.ts)        
s1=student('niloy',16,'cste',77,78,79)
print("total stu-",student.ts)   
s2=student('orna',5,'cste',81,82,83)
print("total stu-",student.ts)   
s1.cal_avg()
s2.cal_avg()
s1.get_grade()
s2.get_grade()
s1.display_info()
s2.display_info()