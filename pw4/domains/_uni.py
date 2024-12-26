"specifically this"
from ._studentcourse import Course, Student

class Uni:
    "uni"

    def __init__(self, name):
        self.name = name
        self.__students = set()
        self.__courses = set()

    @property
    def students(self):
        "set of students"
        return self.__students

    @property
    def courses(self):
        "set of courses"
        return self.__courses

    def _add_course(self, course: Course):
        self.courses.add(course)

    def _add_student(self, student: Student):
        self.students.add(student)


__all__ = ["Uni"]

