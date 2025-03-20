class Student:
    college_name = 'ABC college'     #this is a class attribute
    def __init__(self, name, marks):
        self.name = name             ##this is a Instance attribute
        self.marks = marks           ##this is a Instance attribute
        print('adding new student in Database......')


s1 = Student('karan', 87)
print(s1.college_name)              #also valid for: print(Student.college_name)
print(s1.name, s1.marks)