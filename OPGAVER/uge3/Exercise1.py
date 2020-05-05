import random
import csv
import os


class Student():

    def __init__(self, name, gender, datasheet, imageurl):
        self.name = name
        self.gender = gender
        self.datasheet = datasheet
        self.imageurl = imageurl

    def get_avg_grade(self):
        grades = self.datasheet.get_grades_as_list()
        sumgrades = 0
        for grade in grades:
            sumgrades += int(grade)
        avg = sumgrades/len(grades)
        return avg


class DataSheet():
    def __init__(self, courses=[]):
        self.courses = courses

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            grades.append(course.grade)


class Course():
    def __init__(self, name, classroom, teacher, ECTS, grade: int = None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade


grades = [-3, 0, 2, 4, 7, 10, 12]
classrooms = [101, 103, 105, 107, 109]
ECTS = [5, 10, 20, 30]
courses = ['programming', 'Python',
           'Javascript', 'Illustrator', 'Java', '.Net']
genders = ['male', 'female']
males = ['Hamad', 'Saz', 'Jacob', 'Jabs']
females = ['Fie', 'Katrine', 'Marie']
imgurls = ['https://www.facebook.com/photo.php?fbid=10221448104461408&set=a.1560719067275&type=3&theater',
           'https://www.facebook.com/photo.php?fbid=10207398884321952&set=a.1485306304270&type=3&theater',
           'https://www.facebook.com/photo.php?fbid=10216422367705974&set=a.1482736322599&type=3&theater',
           'https://www.facebook.com/photo.php?fbid=10209872647007077&set=a.1485040580231&type=3&theater',
           'https://www.facebook.com/photo.php?fbid=10221003984672137&set=a.1610497185143&type=3&theater',
           'https://www.facebook.com/photo.php?fbid=10209995111502925&set=a.1597106896131&type=3&theater']


def createStudent(numOfStudents):
    result = []
    result.append(['stud_name', 'course_name', 'teacher',
                   'ects', 'classroom', 'grade', 'img_url'])
