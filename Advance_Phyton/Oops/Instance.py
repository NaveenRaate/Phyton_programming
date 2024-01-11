#creat school , name, location,students
#enoroll_students :- addmision students
#tc students
#list_students=[]

# class School:
#
#     def __init__(self, name='VHS', location='Ballari', students=70):
#         self.name = name
#         self.location = location
#         self.students = students
#
#     def enroll_students(self, num_enroll_students=0):
#         self.num_enroll_students = num_enroll_students
#         self.students = self.num_enroll_students + self.students
#
#     def tc_students(self, num_tc_students=0):
#         self.num_tc_students = num_tc_students
#         self.students = self.students - self.num_tc_students
#
#     def num_students(self):
#         print(f'Number of students enrolled this year:-{self.num_enroll_students} number of students took TC this year:-{self.num_tc_students} Total number of students in the School:-{self.students}')
#
# obj = School()
# obj.enroll_students(20)
# obj.tc_students(5)
# obj.num_students()

############################################################3
# class School:
#
#     def __init__(self, name='VHS', location='Ballari', students=[]):
#         self.name = name
#         self.location = location
#         self.students = students
#
#     def enroll_students(self, new_students=[]):
#         # self.students.append(new_students)
#         self.students += new_students
#         # print(self.students)
#
#     def tc_students(self, tc_students=[]):
#         for student in tc_students:
#             if student in self.students:
#                 self.students.remove(student)
#             else:
#                 continue
#         # print(self.students)
#
#     def list_students(self):
#         print(f'List of students currently in the School:- {self.students}')
#
#
# initial_student_names = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5']
# new_students = ['NewStudent1', 'NewStudent2', 'NewStudent3', 'NewStudent4']
# tc_students = ['Student1', 'Student3']
# obj = School(students=initial_student_names)
# obj.enroll_students(new_students)
# obj.tc_students(tc_students)
# obj.list_students()

##############################################################################################
'''In a single class using intance,class and static method'''

class School:

    welcome = 'Welcome to your new School VHS'

    def __init__(self, name='VHS', location='Ballari', students=[]):
        self.name = name
        self.location = location
        self.students = students

    def enroll_students(self, new_students=[]):
        self.students += new_students

    @classmethod
    def greeting(cls, new_students=[]):
        for student in new_students:
            print(f'Hello {student}, {cls.welcome}')

    def tc_students(self, tc_students=[]):
        for student in tc_students:
            if student in self.students:
                self.students.remove(student)
            else:
                continue

    def list_students(self):
        print(f'List of students currently in the School:- {self.students}')

    @staticmethod
    def farewell(tc_students=[]):
        for student in tc_students:
            print(f'Good luck {student}, wishing you very best for the future!')


initial_student_names = ['Student1', 'Student2', 'Student3', 'Student4', 'Student5']
new_students = ['NewStudent1', 'NewStudent2', 'NewStudent3', 'NewStudent4']
tc_students = ['Student1', 'Student3']
obj = School(students=initial_student_names)
obj.enroll_students(new_students)
obj.tc_students(tc_students)
obj.list_students()
obj.greeting(new_students)
obj.farewell(tc_students)
