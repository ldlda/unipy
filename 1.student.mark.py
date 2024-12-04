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

import copy
import collections
import typing
import sys

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

COURSES_ORIGINAL = copy.deepcopy(COURSES)
STUDENTS_ORIGINAL = copy.deepcopy(STUDENTS)

# functional programming? how do?


def input_course():
    ## convert to number if id is a number
    ## even tho i know its never a number
    """Prompts the user to input a course ID and name, converts the ID to a number if possible, and returns a dictionary with the course details."""
    return {"id": try_convert(input("Course ID: ")), "name": input("Course Name: ")}


# convert to number ahh
def try_convert(s: str) -> int | str:
    """Tries to convert a string to an integer. If it fails, it simply returns the string.

    This is a very simple function that can be used to convert a string to an integer if possible.
    If the conversion fails, it returns the string as is. This is useful when you have a column in a
    database that can contain either a string or an integer, but you want to treat it as an integer
    if possible.

    Args:
        s (str): The string to be converted.

    Returns:
        int | str: The converted integer, or the original string if the conversion fails.
    """
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
    """Prompts the user to input a student ID, name, and date of birth, and returns a dictionary with the student details."""
    return {
        "id": try_convert(input("Student ID: ")),
        "name": input("Student Name: "),
        "DoB": input("Date of Birth: "),
    }


def input_courses():
    """Asks user for number of courses and calls input_course that many times.

    The courses are added to COURSES."""
    for _ in range(int(input("Number of courses: "))):
        input_course()


def input_students():
    """Asks user for number of students and calls input_student that many times.

    The students are added to STUDENTS."""
    for _ in range(int(input("Number of students: "))):
        input_student()


def format_student(student, include_DoB: bool = False, /, short=False):
    """
    Formats a student's information into a string.

    Args:
        student (dict): A dictionary containing student details with keys 'id', 'name', and 'DoB'.
        include_DoB (bool, optional): Whether to include the date of birth in the output. Defaults to False.
        short (bool, optional): Whether to use a short format (name and ID only). Defaults to False.

    Returns:
        str: A formatted string representation of the student's information.
    """
    if short:
        return f"{student['name']} ({student['id']})"
    return f"Student {student['name']} (ID: {student['id']}{' DoB: ' + student['DoB'] if include_DoB else ''})"


# long format and short format?
# get name? get id?
# class? methods? properties? @property @getter @setter ?????
# truly java pilled


def format_course(course, /, short=False):
    """
    Formats a course's information into a string.

    Args:
        course (dict): A dictionary containing course details with keys 'id' and 'name'.
        short (bool, optional): Whether to use a short format (name and ID only). Defaults to False.

    Returns:
        str: A formatted string representation of the course's information.
    """
    if short:
        return f"{course['name']} ({course['id']})"
    return f"Course {course['name']} (ID: {course['id']})"


## now how do i store courses without it blowing up?
## i think i should? change? the format of the STUDENT or COURSE var to a dict for faster?? lookup????
## or else student = next(x in STUDENTS if x.get("id") == student_id) which is ugly definitely ugly
## if students are unique anyways why not make it a dict[id, dict[student info]] which is _also ugly_
## ai tells me its even uglier ngl it is ugly

## i think we are not making postgresql so we dont really need to care about no Performance those are for experts


# STUDENTS_MARKS = collections.defaultdict(dict)

# i think doctring like the other way more:
COURSES_MARKS = collections.defaultdict(dict)

# damn they dont make a difference!! im tripping

## im thinking of an insane, an ABSOLUTELY DERANGED way to do this


def view_mark(course, student):
    """
    Returns the mark for a given student in a given course.

    Args:
        course (dict): A dictionary containing course details with keys 'id' and 'name'.
        student (dict): A dictionary containing student details with keys 'id', 'name', and 'DoB'.

    Returns:
        float | None: The mark for the student in the course, or None if the student has not been marked.
    """
    if COURSES_MARKS[course["id"]].get(student["id"]) is not None:
        return COURSES_MARKS[course["id"]][student["id"]]
    else:
        return None


# format_NA = lambda grade: grade if grade is not None else "N/A"
def format_NA(grade):
    """
    Returns the grade if it is not None, otherwise returns "N/A".

    Args:
        grade (float | None): The grade to be formatted.

    Returns:
        str: The formatted grade.
    """
    return grade if grade is not None else "N/A"


def select_students_to(func: typing.Callable, action: str):
    """
    Iterates over the list of students, prompting the user to select each student for a specified action.

    Args:
        func (typing.Callable): A function to be invoked on each selected student.
        action (str): A description of the action to be performed, used in the prompt message.

    The function displays each student and asks the user to confirm the action with options:
    - 'y': Proceed with the current student.
    - 'n': Skip the current student.
    - 'a': Apply the action to all students without further prompts.
    - 'v': Stop the selection process. No further students will be prompted.
    - Any other input will be treated as 'y'.
    """
    YesNoAlwaysNever = None
    for student in STUDENTS:
        print(f"{format_student(student)}")
        if YesNoAlwaysNever is not True:
            confirm = input(f"Select this student to {action} [Ynav]:").lower()
            match confirm:
                case "a":
                    YesNoAlwaysNever = True
                case "v":  # top 10 things never happen
                    YesNoAlwaysNever = False
                    break  # what else
                case "y":
                    pass
                case "n":
                    continue
                case _:
                    pass
        func(student)


def mark_this_course(course):
    """
    Returns a function to mark students in the given course and a descriptive action string.

    Args:
        course (dict): A dictionary containing course details with keys 'id' and 'name'.

    Returns:
        tuple: A tuple containing:
            - A function that takes a student and marks them for the course.
            - A string describing the action being performed.
    """

    def mark(student):
        return mark_function(student, course)

    return mark, f"mark {format_course(course)}"


add_to_list = (lambda x: x.append, "add to list")

## im so lost
# so am i


## yeah so just realised our COURSES_MARKS work just like the planned STUDENTS_MARKS in our case of use

## that may mean:


def select_courses_to(func: typing.Callable, action: str):
    """
    Iterates over the list of courses, prompting the user to select each course for a specified action.

    Args:
        func (typing.Callable): A function to be invoked on each selected course.
        action (str): A description of the action to be performed, used in the prompt message.

    The function displays each course and asks the user to confirm the action with options:
    - 'y': Proceed with the current course.
    - 'n': Skip the current course.
    - 'a': Apply the action to all courses without further prompts.
    - 'v': Stop the selection process. No further courses will be prompted.
    - Any other input will be treated as 'n'.
    """
    YesNoAlwaysNever = None
    for course in COURSES:
        print(f"{format_course(course)}")
        if YesNoAlwaysNever is not True:
            confirm = input(f"Select this course to {action} [yNav]:").lower()
            match confirm:
                case "a":
                    YesNoAlwaysNever = True
                case "v":
                    YesNoAlwaysNever = False
                    break
                case "y":
                    pass
                case "n":
                    continue
                case _:
                    continue
        func(course)


## bruh im so stupid


def mark_this_student(student):
    """
    Returns a function to mark a course for the given student and a descriptive action string.

    Args:
        student (dict): A dictionary containing student details with keys 'id', 'name', and 'DoB'.

    Returns:
        tuple: A tuple containing:
            - A function that takes a course and marks the student in it.
            - A string describing the action being performed.
    """

    def mark(course):
        return mark_function(student, course)

    return mark, f"mark {format_student(student)}"


# erm is this overengineered?


def mark_function(student, course):
    """
    Prompts the user to input a mark for the given student in the given course.

    Args:
        student (dict): A dictionary containing student details with keys 'id', 'name', and 'DoB'.
        course (dict): A dictionary containing course details with keys 'id' and 'name'.
    """

    print(f"Marking {student['name']} for {course['name']}")
    pre = input("Mark (put blank for N/A): ").strip()
    for _ in range(4):
        try:
            if pre in ["", "N/A"]:
                print("Did not mark")
                return
            mark = float(pre)
        except ValueError:
            print("Invalid mark")
            pre = input("Mark: ").strip()
        else:
            COURSES_MARKS[course["id"]][student["id"]] = mark
            return
    print("cmon how did you fail that much")


# that work too


def view_courses():
    """
    Lists all courses in the database.

    The courses are displayed with their name and ID.
    """
    for course in COURSES:
        # refactor
        print(format_course(course))


def view_students(include_DoB: bool = False):
    """
    Lists all students in the database.

    Args:
        include_DoB (bool, optional): If True, include the date of birth in the output. Defaults to False.

    The students are displayed with their name, ID, and optionally their date of birth.
    """
    for student in STUDENTS:
        print(format_student(student, include_DoB))


def view_marks_for_course(course):
    """
    Lists all marks for a given course.

    Args:
        course (dict): A dictionary containing course details with keys 'id' and 'name'.

    The marks are displayed with the student name, ID, and mark.
    """
    print(f"Mark for course {course['name']} (ID: {course['id']}):")
    for student in STUDENTS:
        print(
            f"\t{format_student(student, short=True)}: {format_NA(view_mark(course, student))}"
        )


def view_marks_for_student(student):
    """
    Lists all marks for a given student.

    Args:
        student (dict): A dictionary containing student details with keys 'id', 'name', and 'DoB'.

    The marks are displayed with the course name, ID, and mark.
    """
    print(f"Mark for student {student['name']} (ID: {student['id']}):")
    for course in COURSES:
        print(
            f"\t{format_course(course, short=True)}: {format_NA(view_mark(course, student))}"
        )


## nothing SCALES omfg ima get no jobs
def _list_fails(course):
    for student_id, marks in COURSES_MARKS[course["id"]].items():
        if marks < 10:
            yield student_id


def search_student(key, value):
    """
    Searches for students in the STUDENTS list based on a specified key and value.

    Args:
        key (str): The key to search for in each student's dictionary (e.g., 'id', 'name', 'DoB').
        value (str): The value to match against the specified key in each student's dictionary.

    Returns:
        generator: A generator yielding students that match the specified key and value.
    """
    return search(lambda student: str(student.get(key)) == str(value), STUDENTS)


## right here!!! this!!!!
def find_student_from_id(student_id):
    """
    Searches for a student in the STUDENTS list based on a specified ID.

    Args:
        id (str or int): The ID to search for in each student's dictionary.

    Returns:
        generator: A generator yielding students that match the specified ID.
    """

    return search(
        lambda student: student.get("id") == try_convert(student_id), STUDENTS
    )


def search_course(key, value):
    """
    Searches for courses in the COURSES list based on a specified key and value.

    Args:
        key (str): The key to search for in each course's dictionary (e.g., 'id', 'name').
        value (str): The value to match against the specified key in each course's dictionary.

    Returns:
        generator: A generator yielding courses that match the specified key and value.
    """
    return search(lambda course: str(course.get(key)) == str(value), COURSES)


# find_course_from_id = lambda id: search(
#     lambda course: course.get("id") == try_convert(id), COURSES
# )


def find_course_from_id(course_id):
    """
    Searches for a course in the COURSES list based on a specified ID.

    Args:
        id (str or int): The ID to search for in each course's dictionary.

    Returns:
        generator: A generator yielding courses that match the specified ID.
    """

    return search(lambda course: course.get("id") == try_convert(course_id), COURSES)


# def search_function(func, collection):
#     for item in collection:
#         if func(item):
#             yield item


# search = lambda func, collection: (
#     item for item in collection if func(item)
# )  # pylint: disable=unnecessary-lambda-assignment # ass


def search(func, collection):
    """
    Applies a given function to each item in a collection, returning a generator yielding only
    the items for which the function evaluates to True.

    Args:
        func (typing.Callable[[typing.Any], bool]): A function that takes an item from the collection and returns a boolean indicating whether the item should be included in the result.
        collection (typing.Iterable[typing.Any]): An iterable collection of items to be processed.

    Yields:
        typing.Any: Items from the collection for which the specified function evaluated to True.
    """
    return (item for item in collection if func(item))


def find():
    """
    Prompts the user to search for either students or courses based on specified criteria.

    The function retrieves user input to determine whether to search for students or courses,
    then prompts for the search key and value. It utilizes search_student or search_course
    accordingly to find and display matching entries. If no matches are found, it notifies
    the user.
    """
    match input("Search for [student|course]: ").casefold():
        case "student":
            if students := search_student(
                input("Key [id|name|dob]: "), input("Value: ")
            ):
                for student in students:
                    print(format_student(student))
            else:
                print("No student found")
        case "course":
            if courses := search_course(input("Key [id|name]: "), input("Value: ")):
                for course in courses:
                    print(format_course(course))
            else:
                print("No course found")
        case _:
            print("Not a valid choice")


def export_to_file(filename):
    """
    Exports the state of the application to a file.

    The application's data, including the list of students, courses, and marks, is
    written to the specified file in plain text format.

    Args:
        filename (str): The path to the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(STUDENTS))
        f.write("\n")
        f.write(str(COURSES))
        f.write("\n")
        f.write(str(COURSES_MARKS))


def import_from_file(filename):
    """
    Imports the state of the application from a file.

    The application's data, including the list of students, courses, and marks, is
    read from the specified file in plain text format.

    Args:
        filename (str): The path to the file to read from.

    Returns:
        tuple: A tuple containing the list of students, courses, and marks,
        in that order.

    Warning:
        This function uses eval() to read the data from the file, which is a
        potential security risk if the file is not trusted.
    """
    with open(filename, "r", encoding="utf-8") as f:
        STUDENTS = eval(f.readline())  # danger
        COURSES = eval(f.readline())
        COURSES_MARKS = eval(f.readline())
    return STUDENTS, COURSES, COURSES_MARKS


def input_cid():
    """
    Prompts the user to input a course ID and returns the corresponding course dictionary.

    The course dictionary is retrieved from the COURSES list using the find_course_from_id() function.

    Args:
        None

    Returns:
        dict or None: The course dictionary if the course ID is found, otherwise None.

    """
    if not (course_id := find_course_from_id(input("Course ID : "))):
        print("Course ID not found")
        return None
    for course_dict in course_id:
        return course_dict


def input_sid():
    """
    Prompts the user to input a student ID and returns the corresponding student dictionary.

    The student dictionary is retrieved from the STUDENTS list using the find_student_from_id() function.

    Args:
        None

    Returns:
        dict or None: The student dictionary if the student ID is found, otherwise None.

    """
    if not (student_id := find_student_from_id(input("Student ID : "))):
        print("Student ID not found")
        return None
    for student_dict in student_id:
        return student_dict


def main():
    """
    The main entry point of the application.

    This function is an infinite loop that continuously displays a menu to the user
    and performs the chosen action. The menu is a simple text-based interface that
    allows the user to mark students in a course, mark courses for a student, view
    marks for a course or student, view all courses or students, find a student or
    course, or exit the application.

    The function uses a match statement to handle the different choices available
    to the user. For each choice, the function either calls another function to
    perform the desired action, or performs the action directly.

    The function is the main entry point of the application and is called by the
    if __name__ == "__main__": block at the end of the file.

    """
    global STUDENTS, COURSES, COURSES_MARKS
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
                if (course_dict := input_cid()) is not None:
                    select_students_to(*mark_this_course(course_dict))
            case "2":
                if (student_dict := input_sid()) is not None:
                    select_courses_to(*mark_this_student(student_dict))
            case "3":
                if (student_dict := input_sid()) is not None and (
                    course_dict := input_cid()
                ) is not None:
                    mark_function(student_dict, course_dict)
            case "4":
                if (course_dict := input_cid()) is not None:
                    view_marks_for_course(course_dict)
            case "5":
                if (student_dict := input_sid()) is not None:
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
                        for _ in range(4):
                            try:
                                input_students()
                                break
                            except ValueError:
                                print("Invalid value")
                    case "2":
                        for _ in range(4):
                            try:
                                input_courses()
                                break
                            except ValueError:
                                print("Invalid value")
                    case "3":
                        export_to_file(input("Filename: "))
                    case "4":
                        STUDENTS, COURSES, COURSES_MARKS = import_from_file(
                            input("Filename: ")
                        )
                    case "9":
                        continue
                    case "0":
                        print("Exiting...")
                        sys.exit()
                    case _:
                        print("Not a valid choice")
                        print("back to the other thingy")
                        continue
                    ## its time to invest into ansi
                    ## and a better way to print in general (good job ai)
            case "0":
                print("Exiting...")
                sys.exit()
            case _:
                print("Not a valid choice")
        print()


if __name__ == "__main__":
    main()
