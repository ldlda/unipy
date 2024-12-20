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
import json
import sys
import typing

# import inspect
# import typing


spec = importlib.util.spec_from_file_location(
    name="student_mark", location="1.student.mark.py"
)

student_mark = importlib.util.module_from_spec(spec)  # type: ignore

spec.loader.exec_module(student_mark)  # type: ignore

# print(inspect.getmembers(student_mark))


# print(student_mark.try_convert("123"))
def also_print(f):
    "decorator to print the return value"

    @functools.wraps(f)
    def w(*a, **kw):
        ret = f(*a, **kw)
        print(f"{f.__name__}({a}, {kw}):", ret)
        return ret

    return w


def todatetime(s: str) -> datetime:
    """converts a string to a datetime object"""
    r: datetime
    er: Exception
    try:
        datetrying = datetime.fromisoformat(s)
    except ValueError as e:
        er = e
    else:
        print("ok nerd")
        r = datetrying
        return r
    finally:
        print(datetrying)

    date_formats = ["%d/%m/%Y", "%d-%m-%Y"]
    for date_format in date_formats:
        try:
            datetrying = datetime.strptime(s, date_format)
        except ValueError as e:
            er = e
        else:
            print(datetrying)
            r = datetrying
            return r
    raise er


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

    def __post_init__(self):
        # if not (self.id and self.name):
        #     raise ValueError("have not specified name or id")
        if not self.id:
            raise ValueError("have not specified id")
        if not self.name:
            raise ValueError("have not specified name")
        if not isinstance(self.id, str):
            super().__setattr__("id", str(self.id))
        if not isinstance(self.name, str):
            super().__setattr__("name", str(self.name))
        if isinstance(self.DoB, str):
            print(
                f"dont do this please: {self.DoB} is {type(self.DoB)}, should be {datetime}"
            )
            super().__setattr__("DoB", todatetime(self.DoB))

        if not isinstance(self.DoB, datetime):
            if not self.DoB:
                raise ValueError("have not specified DoB")
            else:
                raise ValueError("DoB should be datetime")

    def __str__(self):
        return f"Student: {self.name} (ID: {self.id})"


@dataclass(frozen=True)
class Course:
    """
    course dataclass

    id: int
    name: str
    """

    id: str
    name: str

    def __str__(self):
        return f"Course: {self.name} (ID: {self.id})"

    def __post_init__(self):
        # if not (self.id and self.name):
        #     raise ValueError("have not specified name or id")
        if not self.id:
            raise ValueError("id should not be empty")
        if not self.name:
            raise ValueError("name should not be empty")
        if not isinstance(self.id, str):
            super().__setattr__("id", str(self.id))
        if not isinstance(self.name, str):
            super().__setattr__("name", str(self.name))


class Uni(object):
    "what even"

    def __init__(self, name="Uni"):
        self.name = name
        self._STUDENTS = []  # maybe use set
        self._COURSES = []
        self._COURSES_MARKS = collections.defaultdict(dict)

    def __str__(self):
        return f"Uni: {self.name}"

    ## 100% for testing:
    def __repr__(self):
        return self.__str__()

    @property
    def STUDENTS(self):
        return self._STUDENTS

    @STUDENTS.setter
    def STUDENTS(self, value):
        if not isinstance(value, list):
            raise ValueError("STUDENTS should be a list")
        for i in value:
            if not isinstance(i, Student):
                if isinstance(i, dict):
                    i = Student(**i)
                else:
                    raise ValueError("STUDENTS should be a list of Student objects")
        self._STUDENTS = value

    @property
    def COURSES(self):
        return self._COURSES

    @COURSES.setter
    def COURSES(self, value):
        if not isinstance(value, list):
            raise ValueError("COURSES should be a list")
        for i in value:
            if not isinstance(i, Course):
                if isinstance(i, dict):
                    i = Course(**i)
                else:
                    raise ValueError("COURSES should be a list of Course objects")
        self._COURSES = value

    @property
    def COURSES_MARKS(self):
        return self._COURSES_MARKS

    @COURSES_MARKS.setter
    def COURSES_MARKS(self, value):
        self._COURSES_MARKS = value

    def add_student(self, student):
        self.STUDENTS.append(student)

    def add_course(self, course):
        self.COURSES.append(course)

    def add_mark(self, student_id, course_id, mark):
        student_id, course_id = str(student_id), str(course_id)
        self.COURSES_MARKS[student_id][course_id] = mark

    def view_courses(self):
        for course in self.COURSES:
            print(course)
        else:  # pylint: disable=useless-else-on-loop
            print("no courses")

    def view_students(self):
        for student in self.STUDENTS:
            print(student)
        else:  # pylint: disable=useless-else-on-loop # this does have a use
            print("no students")

    def view_marks_for_student(self, student_id):
        student_id = str(student_id)
        for course_id, mark in self.COURSES_MARKS[student_id].items():
            print(f"{course_id}: {mark}")

    def view_marks_for_course(self, course_id):
        course_id = str(course_id)
        for student_id, mark in self.COURSES_MARKS[course_id].items():
            print(f"{student_id}: {mark}")

    @also_print
    def find_student(self, student_id):
        student_id = str(student_id)
        return next(
            (student for student in self.STUDENTS if student.id == student_id), None
        )

    @also_print
    def find_course(self, course_id):
        course_id = str(course_id)
        return next((course for course in self.COURSES if course.id == course_id), None)

    @also_print
    def find_mark(self, student_id, course_id):
        student_id, course_id = str(student_id), str(course_id)
        return self.COURSES_MARKS[student_id].get(course_id)

    def dump(self):
        ## have to handle datetime obj how do i dump that
        def default(o):
            if isinstance(o, datetime):
                return o.date().isoformat()
            return o.__dict__

        s = json.dumps(self, default=default, indent=4)
        return s

    @staticmethod
    def load(json_):
        s = json.loads(json_)
        uni = Uni(s["name"])
        for i in s:
            setattr(uni, i, s[i])

        def ____to(l: list, t: type):
            "ltra mega specific"
            for ind, item in enumerate(l):
                if isinstance(item, dict):
                    l[ind] = t(**item)

        ____to(uni.STUDENTS, Student)
        ____to(uni.COURSES, Course)
        uni.COURSES_MARKS = collections.defaultdict(dict, uni.COURSES_MARKS)
        return uni


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

    d = uni.dump()
    print("uni", d)

    uni2 = Uni.load(d)
    d2 = uni2.dump()
    print("uni2", d2)

    with open("testing/uni1.json", "w", encoding="utf-8") as f:
        f.write(d)
    with open("testing/uni2.json", "w", encoding="utf-8") as f:
        f.write(d2)

    # structure wise d should be equal to d2
    # but python ids man its the python ids
    def recursive_compare(o1, o2):
        if o1 is o2 or o1 == o2:
            return True
        if not isinstance(o1, o2.__class__):
            return False
        if len(o1) != len(o2):
            return False
        print(list(zip(o1, o2)), "\n")
        return all(recursive_compare(a, b) for a, b in zip(o1, o2))

    print(
        "recursive_compare",
        recursive_compare(uni.__dict__.items(), uni2.__dict__.items()),
    )


should_i_be_testing = False
if should_i_be_testing is not False:
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
    "hello"
    print("hello")
    uni = Uni()

    def list_students():
        uni.view_students()

    def list_courses():
        uni.view_courses()

    def add_student():
        print("add student:")
        id_ = input("id: ").strip()
        if not id_:
            print("invalid id")
            return
        name = input("name: ").strip()
        if not name:
            print("invalid name")
            return
        try:
            DoB = todatetime(input("DoB: "))
        except ValueError:
            print("invalid date")
            return
        uni.add_student(Student(id_, name, DoB))

    def add_course():
        print("add course:")
        id_ = input("id: ").strip()
        if not id_:
            print("invalid id")
            return
        name = input("name: ").strip()
        if not name:
            print("invalid name")
            return
        uni.add_course(Course(id_, name))

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
        if s is None:
            print("student not found")
            return
        c = select_course()
        if c is None:
            print("course not found")
            return
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

    def write_to_file():
        print("write to file:")
        namw = input("file name: ").strip()
        try:
            with open(namw, "x", encoding="utf-8") as f:
                f.write(uni.dump())
        except FileExistsError:
            print(f"file of same name ({namw}) already exists")

    def load_from_file() -> Uni | None:
        print("load from file:")
        namw = input("file name: ").strip()
        try:
            with open(namw, "r", encoding="utf-8") as f:
                return Uni.load(f.read())
        except FileNotFoundError:
            print(f"file {namw} not found")
            return None

    ACTIONS = [
        Structure(
            list_students, name="list students", description="lists all students"
        ),
        Structure(list_courses, name="list courses", description="lists all courses"),
        Structure(add_student, name="add student", description="adds a student"),
        Structure(add_course, name="add course", description="adds a course"),
        Structure(mark1, name="mark", description="marks a student for a course"),
        Structure(select_mark1, name="select mark", description="selects a mark"),
        Structure(
            course_marks,
            name="course marks",
            description="lists all marks for a course",
        ),
        Structure(
            student_marks,
            name="student marks",
            description="lists all marks for a student",
        ),
        Structure(
            write_to_file,
            name="write to file",
            description="writes to file, abort if file exists",
        ),
        Structure(load_from_file, name="load from file", description="loads from file"),
        Structure(exit_wrapper, name="exit", description="exits the program"),
    ]

    while True:
        print("\nactions:")
        for i, action in enumerate(ACTIONS):
            print(f"{i}: {action}")
        # print("exit: exits the program")
        try:
            choice = input("type number: ")
            action = ACTIONS[int(choice)]
        except ValueError:
            continue
        except IndexError:
            continue
        try:
            action()
        except Exception as e: #pylint: disable=broad-except
            print("use it correctly bruh")
            print(f"{e.__class__.__name__}: {e}")


if __name__ == "__main__":
    try:
        ui()
    except (KeyboardInterrupt, SystemExit):
        print("bye")
        # raise
    finally:
        print("get out of here")