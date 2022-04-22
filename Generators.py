 #Opgave 1
 
 
from pickle import TRUE
import random


class PythonStudents:


    def __init__(self):
        self.students = []

    def __add__(self, newStudent):
        self.students.append(newStudent)

    def __iter__(self):
        self.index=0
        return self
    
    def __next__(self):
        temp = self.index
        self.index +=1
        if self.index > len(self.students):
            raise StopIteration()
        return self.students[temp]





class Student:

    def __init__(self, name, cpr):
        self.name = name
        self.cpr = cpr

    @property
    def name(self):
            return self.__name

    @name.setter
    def name(self, name):
        self.__name = name.capitalize()

    def __add__(self, student):
            return Student('Anna the daugther', 1234)

    def __str__(self):
            return f'{self.name}, {self.cpr}'

    def __repr__(self):
            return f'{self.__dict__}'



claus = Student("Alexander", 1234)
anna = Student("Anna", 123421)

ps = PythonStudents()
ps + claus
ps + anna

#for i in ps:
    #print(i)


#Opgave 2
names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

def students_list(num_students):
    students = []
    index = 1
    while(True):
        if index >= num_students:
            return students
        student = {'id': index, 'name' : random.choice(names), 'majors': random.choice(majors)}
        students.append(student)
        index+=1

def students_generator(num_students):
    index = 1
    while(True):
        if index >= num_students:
            raise StopIteration()
        student = {'id': index, 'name' : random.choice(names), 'majors': random.choice(majors)}
        yield student
        index+=1

#people = students_list(1000000)
people = students_generator(1000000)
#print(people)