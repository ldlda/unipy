"structs"
from dataclasses import dataclass, field
from datetime import datetime

@dataclass(eq=True, frozen=True)
class Course:
    "course"
    course_id: str = field(default_factory=str, compare=True)
    name: str = field(default_factory=str, compare=False)
    ects: int = field(default_factory=int, compare=False)

    def set_name(self, name: str) -> None:
        "why edit anything at all"
        object.__setattr__(self, "name", name)
    
    def set_ects(self, ects: int) -> None:
        "why use these methods at all"
        object.__setattr__(self, "ects", ects)

@dataclass(frozen = True, eq=True)
class Student:
    "student"
    student_id: str = field(default_factory=str, compare=True)
    name: str = field(default_factory=str, compare=False)
    date_of_birth: datetime = field(default_factory = datetime.now, compare=False)

    def set_name(self, name: str) -> None:
        object.__setattr__(self, "name", name)

    def set_date_of_birth(self, date_of_birth: datetime) -> None:
        object.__setattr__(self, "date_of_birth", date_of_birth)

__all__ = ["Student", "Course"]

def stse():
    "unit test i think idfk"
    course1 = Course("1", "python", 6)
    course2 = Course("2", "java", 8)
    print(course1, course2)
    course3 = Course("2", "webdev", 12)
    print(course3)
    course3.set_name("html")
    course3.set_ects(10)
    print(course3)

    

if __name__ == "__main__":
    stse()