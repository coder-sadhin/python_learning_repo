class Student:
  def __init__(self,name,roll,marks):
   self.name=name
   self.roll=roll
   self.marks=marks

# __str__

student1=Student("Akkas",11,99)
student2=Student("Ali Hasan",22,88)
student3=Student("mahin",44,91)

print(f"Student name is {student1.name}, his roll is {student1.roll}, his marks {student1.marks}")

