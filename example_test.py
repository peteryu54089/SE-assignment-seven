import pytest
import System

def test_login(grading_system):
    name = 'saab'
    courses = ['comp_sci']
    password = 'boomr345'
    grading_system.login(name, password)
    assert grading_system.usr.name == name
    assert grading_system.usr.courses == courses
    assert grading_system.usr.password == password

def test_check_password(grading_system):
    name = 'saab'
    password = 'boomr345'
    assert grading_system.check_password(name, password) == True
    password = 'error'
    assert grading_system.check_password(name, password) == False

# failed
def test_change_grade(grading_system):
    name = 'saab'
    password = 'boomr345'
    grading_system.login(name, password)
    name = 'akend3'
    course = 'comp_sci'
    assignment = 'assignment1'
    grade = 100
    grading_system.usr.change_grade(name, course, assignment, grade)
    assert grading_system.users[name]['courses'][course][assignment]['grade'] == grade

def test_create_assignment(grading_system):
    name = 'saab'
    password = 'boomr345'
    grading_system.login(name, password)
    assignment = 'assignment3'
    due_date = '3/19/22'
    course = 'comp_sci'
    count = len(grading_system.courses[course]['assignments'])
    grading_system.usr.create_assignment(assignment, due_date, course)
    assert len(grading_system.courses[course]['assignments']) == count + 1

# failed
def test_add_student(grading_system):
    name = 'saab'
    password = 'boomr345'
    grading_system.login(name, password)
    name = 'hdjsr7'
    course = 'comp_sci'
    count = len(grading_system.users[name]['courses'])
    grading_system.usr.add_student(name, course)
    assert len(grading_system.users[name]['courses']) == count + 1

def test_drop_student(grading_system):
    name = 'saab'
    password = 'boomr345'
    grading_system.login(name, password)
    name = 'akend3'
    course = 'comp_sci'
    count = len(grading_system.users[name]['courses'])
    grading_system.usr.drop_student(name, course)
    assert len(grading_system.users[name]['courses']) == count - 1

# failed
def test_submit_assignment(grading_system):
    name = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(name, password)
    course = 'cloud_computing'
    assignment = 'assignment1'
    submission = 'new submission'
    submission_date = '1/4/20'
    grading_system.usr.submit_assignment(course, assignment, submission, submission_date)
    assert grading_system.users[name]['courses'][course][assignment]['grade'] == 'N/A'
    assert grading_system.users[name]['courses'][course][assignment]['submission_date'] == submission_date
    assert grading_system.users[name]['courses'][course][assignment]['submission'] == submission
    assert grading_system.users[name]['courses'][course][assignment]['ontime'] == False

# failed
def test_check_ontime(grading_system):
    name = 'hdjsr7'
    password = 'pass1234'
    grading_system.login(name, password)
    submission_date = '1/4/20'
    due_date = '1/3/20'
    assert grading_system.usr.check_ontime(submission_date, due_date) == False

def test_check_grades(grading_system):
    name = 'yted91'
    password = 'imoutofpasswordnames'
    grading_system.login(name, password)
    course = 'software_engineering'
    assert grading_system.usr.check_grades(course) == [['assignment1', 43], ['assignment2', 22]]

# failed
def test_check_grades_with_key_error(grading_system):
    name = 'yted91'
    password = 'imoutofpasswordnames'
    grading_system.login(name, password)
    course = 'cloud_computing'
    assert grading_system.usr.check_grades(course) == [['assignment1', 3], ['assignment2', 5]]

# failed
def test_view_assignments(grading_system):
    name = 'yted91'
    password = 'imoutofpasswordnames'
    grading_system.login(name, password)
    course = 'software_engineering'
    assert grading_system.usr.view_assignments(course) == [['assignment1', '1/1/20'], ['assignment2', '2/1/20']]

# failed
def test_check_password_with_unexisted_user(grading_system):
    name = 'unexisted'
    password = 'boomr345'
    assert grading_system.check_password(name, password) == False

# failed
def test_create_assignment_with_wrong_ta(grading_system):
    name = 'cmhbf5' # cloud_computing, software_engineering
    password = 'bestTA'
    grading_system.login(name, password)
    assignment = 'assignment3'
    due_date = '3/19/22'
    course = 'databases'
    count = len(grading_system.courses[course]['assignments'])
    grading_system.usr.create_assignment(assignment, due_date, course)
    assert len(grading_system.courses[course]['assignments']) == count

# failed
def test_create_assignment_with_wrong_professor(grading_system):
    name = 'saab' # comp_sci
    password = 'boomr345'
    grading_system.login(name, password)
    assignment = 'assignment3'
    due_date = '3/19/22'
    course = 'cloud_computing'
    count = len(grading_system.courses[course]['assignments'])
    grading_system.usr.create_assignment(assignment, due_date, course)
    assert len(grading_system.courses[course]['assignments']) == count

# failed
def test_drop_student_with_wrong_professor(grading_system):
    name = 'saab' # comp_sci
    password = 'boomr345'
    grading_system.login(name, password)
    name = 'hdjsr7'
    course = 'cloud_computing'
    count = len(grading_system.users[name]['courses'])
    grading_system.usr.drop_student(name, course)
    assert len(grading_system.users[name]['courses']) == count

# failed
def test_check_grades_with_wrong_ta(grading_system):
    name = 'cmhbf5' # cloud_computing, software_engineering
    password = 'bestTA'
    grading_system.login(name, password)
    name = 'akend3'
    course = 'databases'
    assert grading_system.usr.check_grades(name, course) == []

# failed
def test_check_grades_with_wrong_professor(grading_system):
    name = 'saab' # comp_sci
    password = 'boomr345'
    grading_system.login(name, password)
    name = 'akend3'
    course = 'databases'
    assert grading_system.usr.check_grades(name, course) == []

@pytest.fixture
def grading_system():
    gradingSystem = System.System()
    gradingSystem.load_data()
    return gradingSystem