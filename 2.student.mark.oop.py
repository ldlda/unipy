"""
redo the last exercise (1.student.mark.py) now with oop
"""

import collections
import importlib
import importlib.machinery
import importlib.util
from dataclasses import dataclass  # , asdict
from datetime import datetime

# import inspect
# import typing

if (
    spec := importlib.util.spec_from_file_location(
        name="student_mark", location="1.student.mark.py"
    ) ## mypy
) is None:
    raise ImportError

if (student_mark := importlib.util.module_from_spec(spec)) is None:
    raise ImportError

if spec.loader is None:
    raise ImportError
spec.loader.exec_module(student_mark)

# print(inspect.getmembers(student_mark))

# print(student_mark.try_convert("123"))


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

    def __init__(self):
        self.STUDENTS = [] # maybe use set
        self.COURSES = []
        self.COURSES_MARKS = collections.defaultdict(dict)
