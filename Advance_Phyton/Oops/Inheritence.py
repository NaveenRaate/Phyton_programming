class School:

    def __init__(self,name, location):
        self.name = name
        self.location = location

    def number_of_students(self):
        print(f'Name of the School {self.name} and location is {self.location}')
        print('Total number of students 70')

class Subjects(School):

    def __int__(self,name,location):
        super().__init__(name,location)

    def subject_details(self):
        print('Total number of subjects :- 8')


obj = Subjects('VHS', 'Ballari')
obj.number_of_students()
obj.subject_details()