"""
redo the last exercise (1.student.mark.py) now with oop
"""

import collections
import functools
import importlib
import importlib.machinery
import importlib.util
from dataclasses import dataclass  # , asdict
import dataclasses
from datetime import datetime
import sys
import typing

# import inspect
# import typing

if (
    spec := importlib.util.spec_from_file_location(
        name="student_mark", location="1.student.mark.py"
    )  ## mypy
) is None:
    raise ImportError

if (student_mark := importlib.util.module_from_spec(spec)) is None:
    raise ImportError

if spec.loader is None:
    raise ImportError
spec.loader.exec_module(student_mark)

# print(inspect.getmembers(student_mark))

# print(student_mark.try_convert("123"))
def also_print(f):
    "decorator to print the return value"
    @functools.wraps(f)
    def w(*a, **kw):
        ret = f(*a, **kw)
        print( f"{f.__name__}({a}, {kw}):",ret)
        return ret
    return w

@dataclass(frozen=True)
class Student:
    """
    student dataclass

    id: int
    name: str
    DoB: datetime
    """

    id: str
    name: str
    DoB: datetime


@dataclass(frozen=True)
class Course:
    """
    course dataclass

    id: int
    name: str
    """

    id: str
    name: str


class Uni:
    "what even"

    def __init__(self, name="Uni"):
        self.name = name
        self.STUDENTS = []  # maybe use set
        self.COURSES = []
        self.COURSES_MARKS = collections.defaultdict(dict)

    def __str__(self):
        return f"Uni: {self.name}"
    
    ## 100% for testing:
    def __repr__(self):
        return self.__str__()
    
    def add_student(self, student):
        self.STUDENTS.append(student)

    def add_course(self, course):
        self.COURSES.append(course)

    def add_mark(self, student_id, course_id, mark):
        self.COURSES_MARKS[student_id][course_id] = mark

    def view_courses(self):
        for course in self.COURSES:
            print(course)

    def view_students(self):
        for student in self.STUDENTS:
            print(student)

    def view_marks_for_student(self, student_id):
        for course_id, mark in self.COURSES_MARKS[student_id].items():
            print(f"{course_id}: {mark}")

    def view_marks_for_course(self, course_id):
        for student_id, mark in self.COURSES_MARKS[course_id].items():
            print(f"{student_id}: {mark}")

    @also_print
    def find_student(self, student_id):
        return next(
            (student for student in self.STUDENTS if student.id == student_id), None
        )

    @also_print
    def find_course(self, course_id):
        return next((course for course in self.COURSES if course.id == course_id), None)

    @also_print
    def find_mark(self, student_id, course_id):
        return self.COURSES_MARKS[student_id].get(course_id)

    


def testing():
    "c"
    # testig
    stA = Student(id=1, name="A", DoB=datetime(2000, 1, 1))
    stB = Student(id=2, name="B", DoB=datetime(2000, 1, 1))
    stC = Student(id=3, name="C", DoB=datetime(2000, 1, 1))
    stD = Student(id=4, name="D", DoB=datetime(2000, 1, 1))
    stE = Student(id=5, name="E", DoB=datetime(2000, 1, 1))
    stF = Student(id=6, name="F", DoB=datetime(2000, 1, 1))
    stG = Student(id=7, name="G", DoB=datetime(2000, 1, 1))

    cA = Course(id=1, name="A")
    cB = Course(id=2, name="B")
    cC = Course(id=3, name="C")
    cD = Course(id=4, name="D")
    cE = Course(id=5, name="E")
    cF = Course(id=6, name="F")
    cG = Course(id=7, name="G")

    uni = Uni()
    uni.STUDENTS = [stA, stB, stC, stD, stE, stF, stG]
    uni.COURSES = [cA, cB, cC, cD, cE, cF, cG]

    uni.add_mark(1, 1, 1)
    uni.add_mark(1, 2, 2)
    uni.add_mark(1, 3, 3)
    uni.add_mark(1, 4, 4)
    uni.add_mark(1, 5, 5)
    uni.add_mark(1, 6, 6)
    uni.add_mark(1, 7, 7)

    uni.add_mark(2, 1, 1)
    uni.add_mark(2, 2, 2)
    uni.add_mark(2, 3, 3)
    uni.add_mark(2, 4, 4)
    uni.add_mark(2, 5, 5)
    uni.add_mark(2, 6, 6)
    uni.add_mark(2, 7, 7)

    uni.add_mark(3, 1, 1)
    uni.add_mark(3, 2, 2)
    uni.add_mark(3, 3, 3)
    uni.add_mark(3, 4, 4)
    uni.add_mark(3, 5, 5)
    uni.add_mark(3, 6, 6)
    uni.add_mark(3, 7, 7)

    uni.add_mark(4, 1, 1)
    uni.add_mark(4, 2, 2)
    uni.add_mark(4, 3, 3)
    uni.add_mark(4, 4, 4)
    uni.add_mark(4, 5, 5)
    uni.add_mark(4, 6, 6)
    uni.add_mark(4, 7, 7)

    uni.add_mark(5, 1, 1)
    uni.add_mark(5, 2, 2)
    uni.add_mark(5, 3, 3)
    uni.add_mark(5, 4, 4)
    uni.add_mark(5, 5, 5)
    uni.add_mark(5, 6, 6)
    uni.add_mark(5, 7, 7)

    uni.add_mark(6, 1, 1)
    uni.add_mark(6, 2, 2)
    uni.add_mark(6, 3, 3)
    uni.add_mark(6, 4, 4)
    uni.add_mark(6, 5, 5)
    uni.add_mark(6, 6, 6)
    uni.add_mark(6, 7, 7)

    uni.add_mark(7, 1, 1)
    uni.add_mark(7, 2, 2)
    uni.add_mark(7, 3, 3)
    uni.add_mark(7, 4, 4)
    uni.add_mark(7, 5, 5)   
    uni.add_mark(7, 6, 6)
    uni.add_mark(7, 7, 7)   

    uni.view_marks_for_student(1)
    uni.view_marks_for_student(2)
    uni.view_marks_for_student(3)
    uni.view_marks_for_student(4)
    uni.view_marks_for_student(5)
    uni.view_marks_for_student(6)
    uni.view_marks_for_student(7)

    uni.view_marks_for_course(1)
    uni.view_marks_for_course(2)
    uni.view_marks_for_course(3)
    uni.view_marks_for_course(4)
    uni.view_marks_for_course(5)
    uni.view_marks_for_course(6)
    uni.view_marks_for_course(7)

    uni.view_students()
    uni.view_courses()

    uni.find_student(1)
    uni.find_student(2)
    uni.find_student(3)
    uni.find_student(4)
    uni.find_student(5)
    uni.find_student(6)
    uni.find_student(7)

    uni.find_course(1)
    uni.find_course(2)
    uni.find_course(3)
    uni.find_course(4)
    uni.find_course(5)
    uni.find_course(6)
    uni.find_course(7)

    uni.find_mark(1, 1)
    uni.find_mark(1, 2)
    uni.find_mark(1, 3)
    uni.find_mark(1, 4)
    uni.find_mark(1, 5)
    uni.find_mark(1, 6)
    uni.find_mark(1, 7)

    uni.find_mark(2, 1)
    uni.find_mark(2, 2)
    uni.find_mark(2, 3)
    uni.find_mark(2, 4)
    uni.find_mark(2, 5)
    uni.find_mark(2, 6)
    uni.find_mark(2, 7)

    uni.find_mark(3, 1)
    uni.find_mark(3, 2)
    uni.find_mark(3, 3)
    uni.find_mark(3, 4)
    uni.find_mark(3, 5)
    uni.find_mark(3, 6)
    uni.find_mark(3, 7)

    uni.find_mark(4, 1)
    uni.find_mark(4, 2)
    uni.find_mark(4, 3)
    uni.find_mark(4, 4)
    uni.find_mark(4, 5)
    uni.find_mark(4, 6)
    uni.find_mark(4, 7)

    uni.find_mark(5, 1)
    uni.find_mark(5, 2)
    uni.find_mark(5, 3)
    uni.find_mark(5, 4)
    uni.find_mark(5, 5)
    uni.find_mark(5, 6)
    uni.find_mark(5, 7)

    uni.find_mark(6, 1)
    uni.find_mark(6, 2)
    uni.find_mark(6, 3)
    uni.find_mark(6, 4)
    uni.find_mark(6, 5)
    uni.find_mark(6, 6)
    uni.find_mark(6, 7)

    uni.find_mark(7, 1)
    uni.find_mark(7, 2)
    uni.find_mark(7, 3)
    uni.find_mark(7, 4)
    uni.find_mark(7, 5)
    uni.find_mark(7, 6)
    uni.find_mark(7, 7)

    uni.find_mark(8, 1)
    uni.find_mark(8, 2)
    uni.find_mark(8, 3)
    uni.find_mark(8, 4)
    uni.find_mark(8, 5)
    uni.find_mark(8, 6)
    uni.find_mark(8, 7)

    uni.find_mark(9, 1)
    uni.find_mark(9, 2)
    uni.find_mark(9, 3)
    uni.find_mark(9, 4)
    uni.find_mark(9, 5)
    uni.find_mark(9, 6)
    uni.find_mark(9, 7)

    uni.find_mark(10, 1)
    uni.find_mark(10, 2)
    uni.find_mark(10, 3)
    uni.find_mark(10, 4)
    uni.find_mark(10, 5)
    uni.find_mark(10, 6)
    uni.find_mark(10, 7)

    uni.find_mark(11, 1)
    uni.find_mark(11, 2)
    uni.find_mark(11, 3)
    uni.find_mark(11, 4)
    uni.find_mark(11, 5)
    uni.find_mark(11, 6)
    uni.find_mark(11, 7)

    uni.find_mark(12, 1)
    uni.find_mark(12, 2)
    uni.find_mark(12, 3)
    uni.find_mark(12, 4)
    uni.find_mark(12, 5)
    uni.find_mark(12, 6)
    uni.find_mark(12, 7)

    uni.find_mark(13, 1)
    uni.find_mark(13, 2)
    uni.find_mark(13, 3)
    uni.find_mark(13, 4)
    uni.find_mark(13, 5)
    uni.find_mark(13, 6)
    uni.find_mark(13, 7)

should_i_be_testing = False
if should_i_be_testing:
    testing()

@dataclass(frozen=True)
class Structure(object):
    func: typing.Callable
    name: str | None = dataclasses.field(default=None, kw_only=True)
    description: str | None = dataclasses.field(default=None, kw_only=True) 

    def __post_init__(self):
        if self.name is None:
            self.name = self.func.__name__

        if self.description is None:
            self.description = self.func.__doc__

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __str__(self):
        return f"{self.name}: {self.description}"


def ui():
    print("hello")
    uni = Uni()
    

    def list_students():
        uni.view_students()

    def list_courses():
        uni.view_courses()

    def add_student():
        print("add student:")
        uni.add_student(
            Student(
                id=input("id: "),
                name=input("name: "),
                DoB=input("DoB: "),
            )
        )

    def add_course():
        print("add course:")
        uni.add_course(
            Course(
                id=input("id: "),
                name=input("name: "),
            )
        )

    def mark(s: Student, c: Course):
        # mark student sdjhgaf asdfkjhg fgjhgk (12313ss) for course cccccccc (225)
        print(f"mark student {s.name} ({s.id}) for course {c.name} ({c.id}):")
        uni.add_mark(
            student_id=s.id,
            course_id=c.id,
            mark=input("mark: "),
        )
    
    def select_student() -> Student:
        print("select student:")
        return uni.find_student(input("id: "))
    
    def select_course() -> Course:
        print("select course:")
        return uni.find_course(input("id: "))

    def select_student_and_course_to(f):
        s = select_student()
        c = select_course()
        f(s, c)
        # when the c++ undefined behavior

    def select_mark(s: Student, c: Course):
        print(f"for student {s.name} ({s.id}) and course {c.name} ({c.id}):")
        mark_ = uni.find_mark(s.id, c.id)
        if mark_ is None:
            print("mark not found")
        else:
            print(f"mark: {mark_.mark}")
    
    def mark1():
        select_student_and_course_to(mark)
    
    def select_mark1():
        print("select mark:")
        select_student_and_course_to(select_mark)

    def course_marks():
        print("course marks:")
        uni.view_marks_for_course(input("id: "))

    def student_marks():
        print("student marks:")
        uni.view_marks_for_student(input("id: "))
    
    def exit_wrapper():
        print("bye", flush=True)
        sys.exit()

    ACTIONS = [
        Structure(list_students, name="list students", description="lists all students"),
        Structure(list_courses, name="list courses", description="lists all courses"),
        Structure(add_student, name="add student", description="adds a student"),
        Structure(add_course, name="add course", description="adds a course"),
        Structure(mark1, name="mark", description="marks a student for a course"),
        Structure(select_mark1, name="select mark", description="selects a mark"),
        Structure(course_marks, name="course marks", description="lists all marks for a course"),
        Structure(student_marks, name="student marks", description="lists all marks for a student"),
        Structure(exit_wrapper, name="exit", description="exits the program"),
    ]

    while True:
        print("\nactions:")
        for i, action in enumerate(ACTIONS):
            print(f"{i}: {action}")
        # print("exit: exits the program")
        try:
            action = ACTIONS[int(input("type number: "))]
        except ValueError:
            continue
        except IndexError:
            continue
        action()

if __name__ == "__main__":
    ui()