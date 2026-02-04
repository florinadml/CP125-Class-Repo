import pytest
import importlib.util
import os

_exercise_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'exercise9.py')
_spec = importlib.util.spec_from_file_location("exercise9_lab6", _exercise_path)
_module = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_module)
find_qualified_students = _module.find_qualified_students

def test_standard_case():
    students = [
        ("S1", {"Math", "Physics", "CS"}),
        ("S2", {"Math", "Physics"}),
        ("S3", {"Math", "Physics", "CS", "English"})
    ]
    required = {"Math", "Physics", "CS"}
    assert find_qualified_students(students, required) == ["S1", "S3"]

def test_all_qualified():
    students = [
        ("S1", {"Math", "Physics"}),
        ("S2", {"Math", "Physics", "English"})
    ]
    required = {"Math", "Physics"}
    assert find_qualified_students(students, required) == ["S1", "S2"]

def test_none_qualified():
    students = [
        ("S1", {"Math"}),
        ("S2", {"Physics"}),
        ("S3", {"English"})
    ]
    required = {"Math", "Physics", "CS"}
    assert find_qualified_students(students, required) == []

def test_single_student_qualified():
    students = [("S1", {"A", "B", "C"})]
    required = {"A", "B"}
    assert find_qualified_students(students, required) == ["S1"]

def test_single_student_not_qualified():
    students = [("S1", {"A", "B"})]
    required = {"A", "B", "C"}
    assert find_qualified_students(students, required) == []

def test_exact_match():
    students = [("S1", {"Math", "Physics"})]
    required = {"Math", "Physics"}
    assert find_qualified_students(students, required) == ["S1"]

def test_sorting_order():
    students = [
        ("Z9", {"A", "B", "C"}),
        ("A1", {"A", "B", "C"}),
        ("M5", {"A", "B", "C"})
    ]
    required = {"A", "B"}
    assert find_qualified_students(students, required) == ["A1", "M5", "Z9"]

def test_empty_students():
    students = []
    required = {"Math", "Physics"}
    assert find_qualified_students(students, required) == []

def test_one_course_required():
    students = [
        ("S1", {"Math", "English"}),
        ("S2", {"Physics"}),
        ("S3", {"Math"})
    ]
    required = {"Math"}
    assert find_qualified_students(students, required) == ["S1", "S3"]

def test_many_extra_courses():
    students = [
        ("S1", {"Math", "Physics", "CS", "Bio", "Chem", "English", "Art"}),
        ("S2", {"Math", "Physics"})
    ]
    required = {"Math", "Physics", "CS"}
    assert find_qualified_students(students, required) == ["S1"]
