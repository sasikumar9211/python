class Student:

    def __init__(self,name,grades):
        self.name = name
        self.grades = grades
    

    def average_grades(self):
        return sum(self.grades)/len(self.grades)
    
student1 = Student("Bob",(100,77,82,88,85))
student2 = Student("Rolf",(90,83,87,95,96))

print(student1.average_grades()) 
print(student2.average_grades()) 