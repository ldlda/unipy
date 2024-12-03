"""student mark management
Build a student mark management system

Functions
• Input functions:
    • Input number of students in a class
    • Input student information: id, name, DoB
    • Input number of courses
    • Input course information: id, name
    • Select a course, input marks for student in this course
• Listing functions:
    • List courses
    • List students
    • Show student marks for a given course

use no objects/classes (impossible??)

fun times
"""

## should make up some courses

## courses are added by me not by code users thanks
COURSES = [
    {"id": 1, "name": "Advanced Programming with Python"},
    {"id": 2, "name": "Fundametals of Databases"},
    {"id": 3, "name": "Algebraic Structures"},
    {"id": 4, "name": "Data Structures and Algorithms"},
    {"id": 5, "name": "Computer Networks"},
    {"id": 6, "name": "Object Oriented Programming"},
    {"id": 7, "name": "Operating Systems"},
    {"id": 8, "name": "Software Engineering"},
    {"id": 9, "name": "Fundamentals of Optimization"},
]

## ig

## made up students? i think so

STUDENTS = [
    {"id": 1, "name": "Anh", "DoB": "01/01/2000"},
    {"id": 2, "name": "Binh", "DoB": "02/02/2000"},
    {"id": 3, "name": "Chinh", "DoB": "03/03/2000"},
    {"id": 4, "name": "Duc", "DoB": "04/04/2000"},
    {"id": 5, "name": "Erik", "DoB": "05/05/2000"},
    {"id": 6, "name": "Felix", "DoB": "06/06/2000"},
    {"id": 7, "name": "Giang", "DoB": "07/07/2000"},
    {"id": 8, "name": "Hieu", "DoB": "08/08/2000"},
    {"id": 9, "name": "Ivan", "DoB": "09/09/2000"},
    {"id": 10, "name": "Jing", "DoB": "10/10/2000"},
]

# :fire:

## data bases manage ment

## each student id has a list of marks
# conflicted ahh
## i either do this either for Marks for a given course, or Marks for a given student,
## and then use lambda function to hit the other one.
## idk how any of the choices above is efficient at all,
## OR make a both and update both which: is not a better choice in the slightest

# wing

## damn mr coder is stupid courses ARE added by the user, as intended in docstring.

## COURSES_ORIGINAL ahh
import copy

COURSES_ORIGINAL = copy.deepcopy(COURSES)
STUDENTS_ORIGINAL = copy.deepcopy(STUDENTS)

# functional programming? how do?


def input_courses():
    for i in range(int(input("Number of courses: "))):
        input_course()


def input_students():
    for i in range(int(input("Number of students: "))):
        input_student()


def input_course():
    ## convert to number if id is a number
    ## even tho i know its never a number
    return {"id": try_convert(input("Course ID: ")), "name": input("Course Name: ")}


# convert to number ahh
def try_convert(s: str) -> int | str:
    try:
        return int(s)
    except ValueError:
        return s
    # cmon


# i would debate that this isnt a good idea,
# you see in a database like postgres a column can only have one type. And it is for a reason. a good reason.
# to do this conversion just adds complexity

# however! idc


def input_student():
    return {
        "id": try_convert(input("Student ID: ")),
        "name": input("Student Name: "),
        "DoB": input("Date of Birth: "),
    }


def format_student(student, include_DoB: bool = False, /, short=False):
    if short:
        return f"{student['name']} ({student['id']})"
    return f"Student {student['name']} (ID: {student['id']}{' DoB: ' + student['DoB'] if include_DoB else ''})"


# long format and short format?
# get name? get id?
# class? methods? properties? @property @getter @setter ?????
# truly java pilled


def format_course(course, /, short=False):
    if short:
        return f"{course['name']} ({course['id']})"
    return f"Course {course['name']} (ID: {course['id']})"


## now how do i store courses without it blowing up?
## i think i should? change? the format of the STUDENT or COURSE var to a dict for faster?? lookup????
## or else student = next(x in STUDENTS if x.get("id") == student_id) which is ugly definitely ugly
## if students are unique anyways why not make it a dict[id, dict[student info]] which is _also ugly_
## ai tells me its even uglier ngl it is ugly

## i think we are not making postgresql so we dont really need to care about no Performance those are for experts

import collections
import typing

# STUDENTS_MARKS = collections.defaultdict(dict)

# i think doctring like the other way more:
COURSES_MARKS = collections.defaultdict(dict)

# damn they dont make a difference!! im tripping

## im thinking of an insane, an ABSOLUTELY DERANGED way to do this


def view_mark(course, student):
    if COURSES_MARKS[course["id"]].get(student["id"]) is not None:
        return COURSES_MARKS[course["id"]][student["id"]]
    else:
        return None


format_NA = lambda grade: grade if grade is not None else "N/A"


def select_students_to(func: typing.Callable, action: str):
    for student in STUDENTS:
        if (
            input(
                f"""
        {format_student(student)}
        Select this student to {action} [yN]:
        """
            ).lower()
            == "y"
        ):
            ## damn i would love for f to hold the [something] or some sort idfk
            func(student)


def mark_this_course(course):
    def mark(student):
        return mark_function(student, course)

    return mark, f"mark {format_course(course)}"


add_to_list = (lambda x: lambda y: x.append(y), "add to list")

## im so lost
# so am i


## yeah so just realised our COURSES_MARKS work just like the planned STUDENTS_MARKS in our case of use

## that may mean:


def select_courses_to(func: typing.Callable, action: str):
    for course in COURSES:
        if (
            input(
                f"""
        {format_course(course)}
        Select this course to {action} [yN]:
        """
            ).lower()
            == "y"
        ):
            func(course)


## bruh im so stupid


def mark_this_student(student):
    def mark(course):
        return mark_function(student, course)

    return mark, f"mark {format_student(student)}"


# erm is this overengineered?


def mark_function(student, course):
    print(f"Marking {student['name']} for {course['name']}")
    for _ in range(5):
        try:
            mark = float(input("Mark: "))
        except ValueError:
            print("Invalid mark")
        else:
            COURSES_MARKS[course["id"]][student["id"]] = mark
            return
    print("bro cant type a number right god damn")
    print("quit life")
    exit(1)  # lmao


# that work too


def view_courses():
    for course in COURSES:
        # refactor
        print(format_course(course))


def view_students(include_DoB: bool = False):
    for student in STUDENTS:
        print(format_student(student, include_DoB))


def view_marks_for_course(course):
    print(f"Mark for course {course['name']} (ID: {course['id']}):")
    for student in STUDENTS:
        print(
            f"\t{format_student(student, short=True)}: {format_NA(view_mark(course, student))}"
        )


def view_marks_for_student(student):
    print(f"Mark for student {student['name']} (ID: {student['id']}):")
    for course in COURSES:
        print(
            f"\t{format_course(course, short=True)}: {format_NA(view_mark(course, student))}"
        )


## nothing SCALES omfg ima get no jobs
def list_fails(course):
    for student_id, marks in COURSES_MARKS[course["id"]].items():
        if marks < 10:
            yield student_id


def search_student(key, value):
    return [search(lambda student: student.get(key) == value, STUDENTS)]


## right here!!! this!!!!
def find_student_from_id(id):
    return search(lambda student: student.get("id") == try_convert(id), STUDENTS)


def search_course(key, value):
    return list(search(lambda course: course.get(key) == value, COURSES))


find_course_from_id = lambda id: search(
    lambda course: course.get("id") == try_convert(id), COURSES
)


def search(func, collection):
    for item in collection:
        if func(item):
            yield item


search_l = lambda func, collection: (item for item in collection if func(item))


def find():
    match input("Search for: ").casefold():
        case "student":
            for student in search_student(
                input("Key [id|name|dob]: "), input("Value: ")
            ):
                print(format_student(student))
        case "course":
            for course in search_course(input("Key [id|name]: "), input("Value: ")):
                print(format_course(course))
        case _:
            print("Not a valid choice")


def export_to_file(filename):
    with open(filename, "w") as f:
        f.write(str(STUDENTS))
        f.write("\n")
        f.write(str(COURSES))
        f.write("\n")
        f.write(str(COURSES_MARKS))


def import_from_file(filename):
    with open(filename, "r") as f:
        STUDENTS = eval(f.readline())  # danger
        COURSES = eval(f.readline())
        COURSES_MARKS = eval(f.readline())
    return STUDENTS, COURSES, COURSES_MARKS


def main():
    while True:
        print(
            """What do you want to do?
\t1. Mark students in a course
\t2. Mark courses for a student
\t3. Mark a student in a course
\t4. View marks for a course
\t5. View marks for a student
\t6. View all courses
\t7. View all students
\t8. Find a student or course
\t9. More options...
\t0. Exit
"""
        )
        choice = input("Choice: ")
        print()
        match choice:
            case "1":
                course_id = input("Course ID : ")
                if not (course_id := find_course_from_id(course_id)):
                    print("Course ID not found")
                else:
                    for course_dict in course_id:
                        select_students_to(*mark_this_course(course_dict))

            case "2":
                student_id = input("Student ID : ")
                if not (student_id := find_student_from_id(student_id)):
                    print("Student ID not found")
                else:
                    for student_dict in student_id:
                        select_courses_to(*mark_this_student(student_dict))

            case "3":
                student_id = input("Student ID : ")
                if not (student_id := find_student_from_id(student_id)):
                    print("Student ID not found")
                    break
                course_id = input("Course ID : ")
                if not (course_id := find_course_from_id(course_id)):
                    print("Course ID not found")
                    break
                for student_dict in student_id:  # O(1)
                    for course_dict in course_id:  # O(1)
                        mark_function(student_dict, course_dict)  # still O(1)
            case "4":
                course_id = input("Course ID : ")
                if not (course_id := find_course_from_id(course_id)):
                    print("Course ID not found")
                else:
                    for course_dict in course_id:
                        view_marks_for_course(course_dict)
            case "5":
                student_id = input("Student ID : ")
                if not (student_id := find_student_from_id(student_id)):
                    print("Student ID not found")
                else:
                    for student_dict in student_id:
                        view_marks_for_student(student_dict)
            case "6":
                view_courses()
            case "7":
                view_students()
            case "8":
                find()
            case "9":
                print(
                    """\t1. Add students
\t2. Add courses
\t3. Export to file (experimental)
\t4. Import from file (experimental)
\t9. Back
\t0. Exit"""
                )
                choice = input("Choice: ")
                match choice:
                    case "1":
                        input_students()
                    case "2":
                        input_courses()
                    case "3":
                        export_to_file(input("Filename: "))
                    case "4":
                        STUDENTS, COURSES, COURSES_MARKS = import_from_file(
                            input("Filename: ")
                        )
                    case "9":
                        continue
                    case "0":
                        exit()
                    case _:
                        print("Not a valid choice")
                        print("back to the other thingy")
                        continue
                    ## its time to invest into ansi
                    ## and a better way to print in general (good job ai)
            case "0":
                exit()
            case _:
                print("Not a valid choice")
        print()


if __name__ == "__main__":
    main()
