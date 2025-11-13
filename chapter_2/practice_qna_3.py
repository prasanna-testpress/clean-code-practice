#3Question 3

def handle(data):
    total = 0
    for d in data:
        total += d["v"]
    return total / len(data)


#my answer
from typing import List,Dict

def find_total_mark(students:List[Dict[str,int]] )->int:

    total=0

    for student in students:

        total += student["mark"]

def find_average_student_mark(students:List[Dict[str,int]])->float:

    total_mark = find_total_mark(students)
    num_of_student=len(students)

    return (total_mark/num_of_student)


#refactor

from typing import List, Dict, Optional

def calculate_total_marks(students: List[Dict[str, int]]) -> int:
    """Return the total marks of all students."""
    total = 0
    for student in students:
        total += student["mark"]
    return total

def calculate_average_mark(students: List[Dict[str, int]]) -> Optional[float]:
    """Return the average mark of all students, or None if list is empty."""
    if not students:
        return None
    
    total_marks = calculate_total_marks(students)
    num_of_students = len(students)
    return total_marks / num_of_students
