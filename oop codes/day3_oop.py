class Student:
    ts=0
   
    def __init__(self,name,roll,dept,marks):
        self.name=name
        self.roll=roll
        self.dept=dept
        self.marks=marks
        Student.ts+=1
        # self.cal_avg()
        # self.get_grade()

    @property
    def marks(self):
        return self._marks
  

    @marks.setter
    def marks(self, values):      
        for mark in values:
            if not(0 <= mark <= 100):
                print("Invalid marks- ", mark)
                return
        self._marks = values

    @property    
    def avg(self):
        return sum(self._marks) / len(self._marks)

    @property    
    def grade(self):
        avg = self.avg
        if avg>=80:
            return 'A'
        elif avg>=70:
            return 'B'
        elif avg>=60:
            return 'C'
        else:
            return 'F'
        
    def display_info(self):
        
        print("name- ", self.name)
        print("roll- ", self.roll)
        print("avg mark- ", self.avg)
        print("grade- ", self.grade)

    @classmethod
    def show_ts(cls):
        print("total student-",cls.ts)
        
        
print("total stu-",Student.ts)        
s1=Student('niloy',16,'cste',[77,78,79])
#print("total stu-",Student.ts)   
s2=Student('orna',5,'cste',[81,82,83])
#print("total stu-",Student.ts)   

s1.display_info()
s2.display_info()
Student.show_ts()

s1.marks = [95, 80, 85]
s1.display_info()
